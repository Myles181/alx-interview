#!/usr/bin/python3
"""
Vlidation of UTF8 encoding
"""


def validUTF8(data):
     """
     Initialize a variable to keep track of the number of bytes in the current character
     """
    bytes_to_read = 0

    for num in data:
        # Check if the most significant bit of the current byte is 0
        if num & 0x80 == 0:
            if bytes_to_read > 0:
                return False  # Invalid continuation byte
        elif num & 0xC0 == 0x80:
            if bytes_to_read == 0:
                return False  # Invalid start of a character
            bytes_to_read -= 1
        else:
            if bytes_to_read > 0:
                return False  # Invalid continuation byte
            if num & 0xE0 == 0xC0:
                bytes_to_read = 1
            elif num & 0xF0 == 0xE0:
                bytes_to_read = 2
            elif num & 0xF8 == 0xF0:
                bytes_to_read = 3
            else:
                return False  # Invalid start of a character

    return bytes_to_read == 0  # All characters were properly terminate

