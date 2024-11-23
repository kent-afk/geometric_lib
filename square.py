
def area(a):
    if (a < 0):
        raise ValueError("Can't use negative numbers")

    return a * a


def perimeter(a):
    if (a < 0):
        raise ValueError("Can't use negative numbers")  # added verification of borders cuz them cant be below zeros
    return 4 * a
