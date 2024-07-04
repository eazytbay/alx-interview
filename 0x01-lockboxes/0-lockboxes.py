#!/usr/bin/python3
"""This is a method used to determine if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """function that keeps track of which boxes are unlocked"""
    boxes_unlocked = {0}
    # A queue to keep track of the boxes to be opened
    sequence = [0]

    while sequence:
        box = sequence.pop(0)
        # loop through all the keys in the current box
        for key in boxes[box]:
            # check if the key opens a box that has not been unlocked yet
            if key < len(boxes) and key not in boxes_unlocked:
                # sum up the box to the set of unlocked boxes
                boxes_unlocked.add(key)
                # sum up the box to the queue of boxes to be opened
                sequence.append(key)

    # check if all boxes have been unlocked
    return len(boxes_unlocked) == len(boxes)
