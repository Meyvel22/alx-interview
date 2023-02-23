#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """a method that determines if a given data set
    represents a valid utf-8 encoding
    """
    digit_bytes = 0

    mask_01 = 1 << 7
    mask_02 = 1 << 6

    for x in data:

        mask_byte = 1 << 7

        if digit_bytes == 0:

            while mask_byte & x:
                digit_bytes += 1
                mask_byte = mask_byte >> 1

            if digit_bytes == 0:
                continue

            if digit_bytes == 1 or digit_bytes > 4:
                return False

        else:
            if not (x & mask_01 and not (x & mask_02)):
                return False

        digit_bytes -= 1

    if digit_bytes == 0:
        return True

    return False
