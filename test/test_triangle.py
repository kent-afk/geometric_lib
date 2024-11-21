from triangle import *


def test_area():
    test_cases = [
        (3, 4, 5, 6),
        (6, 8, 10, 24),
        (10, 10, 10, 43.30127018922193),
    ]
    for a, b, c, expected in test_cases:
        res = area(a, b, c)
        assert res == expected


def test_negative_area():
    test_cases = [
        (-12, -2, -3, False),
        (30, 2, 1, False),
        (15, 13, 1, False)
    ]
    for a, b, c, expected in test_cases:
        res = area(a, b, c)
        assert res == expected


def test_perimeter():
    test_cases = [
        (3, 4, 5, 12),
        (6, 8, 10, 24),
        (10, 10, 10, 30),
    ]
    for a, b, c, expected in test_cases:
        res = perimeter(a, b, c)
        assert res == expected


def test_negative_perimeter():
    test_cases = [
        (-12, -2, -3, False),
        (30, 2, 1, False),
        (15, 13, 1, False)
    ]
    for a, b, c, expected in test_cases:
        res = perimeter(a, b, c)
        assert res == expected
