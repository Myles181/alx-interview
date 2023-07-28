#!/usr/bin/python3
"""
    Pascal's Triangle is an arrangement of numbers
    in a triangular(nested) array such that the numbers at
    the end of each row are 1 and the remaining 
    numbers are the sum of the nearest two numbers
    in the above row
"""

def pascal_triangle(n):

    """ pascal_triangle: 
            Args: n - n is the number of rows
            Returns: list of lists of integers
    """
    if n <= 0:
        return []
    if not isinstance(n, int):
        print("Input an integer")
        return -1
    array = []

    # Traverse i to the range of n && j to the range of i+1
    for i in range(n):
        temp = []
        for j in range(i+1):
            # If j = 0 means we're at the beginning of the list
            # If j = i means we're at the end of the list
            # Hence we add 1
            if j == 0 or j == i:
                temp.append(1)
            else:
                # We sum the two nearest numbers above the current position
                v = array[i-1][j-1] + array[i-1][j]
                temp.append(v)

        array.append(temp)

    return array
