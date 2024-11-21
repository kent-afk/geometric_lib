
def area(a):
    if (a < 0):
        return False

    return a * a


def perimeter(a):
    if (a < 0):
        return False  # added verification of borders cuz them cant be below zeros
    return 4 * a
