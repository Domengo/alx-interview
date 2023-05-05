#!/usr/bin/env python3
"""return an integer"""

def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    h_count = 1
    clipboard = 1

    while h_count < n:
        if n % h_count == 0:
            clipboard = h_count
        h_count += clipboard
        operations += 1

    if h_count == n:
        return operations
    else:
        return 0

