import math


def area(r):
    if (r < 0):
        raise ValueError("Can't use negative numbers")  # added verification of data
    return math.pi * r * r


def perimeter(r):
    if (r < 0):
        raise ValueError("Can't use negative numbers")
    return 2 * math.pi * r
