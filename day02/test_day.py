import pytest

from main import parse, validate, validate_occurance


def test_parse():
    assert parse("1-3 a: abcde") == {"low": 1, "high": 3, "letter": "a", "pw": "abcde"}
    assert parse("1-3 b: cdefg") == {"low": 1, "high": 3, "letter": "b", "pw": "cdefg"}
    assert parse("2-9 c: ccccccccc") == {
        "low": 2,
        "high": 9,
        "letter": "c",
        "pw": "ccccccccc",
    }
    assert parse("2-10 c: ccccccccc") == {
        "low": 2,
        "high": 10,
        "letter": "c",
        "pw": "ccccccccc",
    }


def test_validate():
    assert validate(parse("1-3 a: abcde"))
    assert not validate(parse("1-3 b: cdefg"))
    assert validate(parse("2-9 c: ccccccccc"))
    assert not validate(parse("2-9 c: cccccccccccc"))
    assert not validate(parse("8-9 f: ffqfffflf"))


def test_validate_occurance():
    assert validate_occurance(parse("1-3 a: abcde"))
    assert not validate_occurance(parse("1-3 b: cdefg"))
    assert validate_occurance(parse("1-3 e: cdefg"))
    assert not validate_occurance(parse("2-9 c: ccccccccc"))
    assert not validate_occurance(parse("2-10 c: ccccccccc"))
