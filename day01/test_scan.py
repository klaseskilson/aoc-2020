import pytest

from main import scan2d, scan3d


def test_scan2d():
    entries = [1721, 979, 366, 299, 675, 1456]
    a, b = scan2d(entries)


def test_scan3d():
    entries = [1721, 979, 366, 299, 675, 1456]
    a, b, c = scan3d(entries)
    assert a * b * c == 241861950
