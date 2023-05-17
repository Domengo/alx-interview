#!/usr/bin/env python3
"""a method that determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    num_bytes = 0
    for byte in data:
        # If num_bytes is 0, we are starting a new character
        if num_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            if byte >> 7 == 0b0:
                num_bytes = 1
            elif byte >> 5 == 0b110:
                num_bytes = 2
            elif byte >> 4 == 0b1110:
                num_bytes = 3
            elif byte >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If there are remaining bytes, it's an invalid encoding
    return num_bytes == 0
