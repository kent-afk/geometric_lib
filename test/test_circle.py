import math
from circle import *


def test_area():
    test_cases = [
        (1, 1 * math.pi),
        (0, 0),
        (2, 4 * math.pi)
    ]
    for rad, expected in test_cases:
        res = area(rad)
        assert res == expected


def test_negative_area():
    test_cases = [
        (-12, False),
        (-235, False),
        (-1, False)
    ]
    for rad, expected in test_cases:
        res = area(rad)
        assert res == expected


def test_perimeter():
    test_cases = [
        (1, 2 * math.pi),
        (0, 0),
        (2, 4 * math.pi)
    ]
    for radius, expected in test_cases:
        res = perimeter(radius)
        assert res == expected


def test_negative_perimeter():
    test_cases = [
        (-12, False),
        (-235, False),
        (-1, False)
    ]
    for rad, expected in test_cases:
        res = perimeter(rad)
        assert res == expected
