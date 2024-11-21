import math


def area(r):
    if (r < 0):
        return False  # added verification of data
    return math.pi * r * r


def perimeter(r):
    if (r < 0):
        return False
    return 2 * math.pi * r
