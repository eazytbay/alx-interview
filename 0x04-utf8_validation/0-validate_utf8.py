#!/usr/bin/python3
"""
Task on UTF-8 Validation
"""


def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    count_byte = 0

    for x in data:
        if count_byte == 0:
            if x >> 5 == 0b110 or x >> 5 == 0b1110:
                count_byte = 1
            elif x >> 4 == 0b1110:
                count_byte = 2
            elif x >> 3 == 0b11110:
                count_byte = 3
            elif x >> 7 == 0b1:
                return False
        else:
            if x >> 6 != 0b10:
                return False
            count_byte -= 1
    return count_byte == 0
