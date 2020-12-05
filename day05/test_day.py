import pytest

from main import search, get_seat


def test_column():
    assert search("RRR", [0, 7]) == 7
    assert search("RRL", [0, 7]) == 6
    assert search("RLR", [0, 7]) == 5
    assert search("RLL", [0, 7]) == 4
    assert search("LRR", [0, 7]) == 3
    assert search("LRL", [0, 7]) == 2
    assert search("LLR", [0, 7]) == 1
    assert search("LLL", [0, 7]) == 0


def test_row():
    assert search("BFFFBBF", [0, 127]) == 70
    assert search("FBFBBFF", [0, 127]) == 44
    assert search("BFFFBBB", [0, 127]) == 71
    assert search("FFFBBBF", [0, 127]) == 14
    assert search("BBFFBBF", [0, 127]) == 102
    assert search("BBFFBBB", [0, 127]) == 103


def test_seat():
    assert get_seat("BFFFBBFRRR") == 567
    assert get_seat("FFFBBBFRRR") == 119
    assert get_seat("BBFFBBFRLL") == 820
