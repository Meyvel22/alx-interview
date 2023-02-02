#!/usr/bin/python3
"""A method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """This function will take a list of lists (boxes) and the content
       will unlock other boxes eventhough not all will be opened
    """

    ans = [0]
    for key in ans:
        for boxKey in boxes[key]:
            if boxKey not in ans and boxKey < len(boxes):
                ans.append(boxKey)
    if len(ans) == len(boxes):
        return True
    return False
