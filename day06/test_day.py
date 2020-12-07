import pytest

from main import count, count_unified


def test_count():
    assert count("abc") == 3
    assert count("a\nb\nc") == 3
    assert count("a\na\na") == 1
    assert count("ab\nac") == 3


def test_count_unified():
    assert count_unified("abc") == 3
    assert count_unified("a\nb\nc") == 0
    assert count_unified("ab\nac") == 1
    assert count_unified("a\na\na") == 1
    assert count_unified("b") == 1
