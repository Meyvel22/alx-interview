#!/usr/bin/python3
"""Module to return pascal triangle """


def pascal_triangle(n):
    """
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    """
    index = []
    if n == 0:
        return index
    for x in range(n):
        index.append([])
        index[x].append(1)
        if (x > 0):
            for y in range(1, x):
                index[x].append(index[x - 1][y - 1] + index[x - 1][y])
            index[x].append(1)
    return index
