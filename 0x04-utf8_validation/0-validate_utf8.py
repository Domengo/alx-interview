#!/usr/bin/env python3
"""a method that determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    num_bytes = 0
    for byte in data:
        # If num_bytes is 0, we are starting a new character
        mask = 1 << 7
        if not num_bytes:
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If there are remaining bytes, it's an invalid encoding
    return num_bytes == 0
