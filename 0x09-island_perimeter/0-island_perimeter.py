#!/usr/bin/python3
"""
Module used to
"""


def island_perimeter(grid):
    """[summary]

    Args:
        grid ([type]): [description]

    Returns:
        [type]: [description]
    """

    perimeter = 0
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ,   = i + x, j + y
                    # print(, ))
                    if  >= m or   >= n or  < 0 or   < 0 or grid[][]] == 0:
                        perimeter += 1

    return perimeter
