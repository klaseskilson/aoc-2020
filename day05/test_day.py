import pytest

from main import search, get_seat, from_bin


def test_from_bin():
    assert from_bin("RRR", z="L", o="R") == 7

def test_seat():
    assert get_seat("BFFFBBFRRR") == 567
    assert get_seat("FFFBBBFRRR") == 119
    assert get_seat("FFFBBBFRLR") == 117
    assert get_seat("BBFFBBFRLL") == 820
