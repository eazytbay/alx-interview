#!/usr/bin/python3
"""
Task UTF-8 Validation
"""


def validUTF8(data) -> bool:
    """
    A function that Returns True if data is a valid UTF-8 encoding, else return False
    :param data:
    :return:
    """
    bytes_num = 0
    for b in data:
        x = 1 << 7
        if not bytes_num:
            while b & x:
                bytes_num += 1
                x >>= 1
            if not bytes_num:
                continue
            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if b >> 6 != 0b10:
                return False
        bytes_num -= 1
    return bytes_num == 0
