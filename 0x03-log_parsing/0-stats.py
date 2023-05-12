#!/usr/bin/env python3
"""Log parsing"""
import sys


# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}

# Helper function to parse status code from log line
def get_status_code(line):
    try:
        status_code = int(line.split()[8])
        return status_code
    except (IndexError, ValueError):
        return None

# Loop through stdin line by line
for i, line in enumerate(sys.stdin):
    # Ignore lines that don't match expected format
    if not line.startswith('"GET /projects/260'):
        continue

    # Extract file size from log line
    try:
        file_size = int(line.split()[9])
    except (IndexError, ValueError):
        continue

    # Add file size to total
    total_file_size += file_size

    # Count status codes
    status_code = get_status_code(line)
    if status_code is not None:
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

    # Print metrics every 10 lines or on keyboard interruption
    if i % 10 == 9:
        print("Total file size: File size:", total_file_size)
        for status_code in sorted(status_code_counts.keys()):
            print(status_code, ":", status_code_counts[status_code])

    try:
        # Check for keyboard interruption
        if sys.stdin.isatty() and sys.stdin.read(1) == '\x03':
            break
    except KeyboardInterrupt:
        break

# Print final metrics
print("Total file size: File size:", total_file_size)
for status_code in sorted(status_code_counts.keys()):
    print(status_code, ":", status_code_counts[status_code])
