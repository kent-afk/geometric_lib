from square import *
import pytest


def test_area():
    test_cases = [
        (1, 1),
        (2, 4),
        (5, 25)
    ]
    for border, expected in test_cases:
        res = area(border)
        assert res == expected


def test_negative_area():
    test_cases = [
        (-12),
        (-235),
        (-1)
    ]
    for border in test_cases:
        with pytest.raises(ValueError):
            area(border)


def test_perimeter():
    test_cases = [
        (1, 4),
        (2, 8),
        (5, 20)
    ]
    for border, expected in test_cases:
        res = perimeter(border)
        assert res == expected


def test_negative_perimeter():
    test_cases = [
        (-12),
        (-235),
        (-1)
    ]
    for border in test_cases:
        with pytest.raises(ValueError):
            perimeter(border)
