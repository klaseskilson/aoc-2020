import pytest

from main import Map

M = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


# def test_map_print():
#     t = Map.from_input(M)
#     assert t.p() == str(M)


def test_map_size():
    t = Map.from_input(M)
    assert t.size() == [11, 11]


def test_count():
    t = Map.from_input(M)
    moves = 10
    c = 0
    for i in range(moves):
        t.move()
        if t.curr() == "#":
            c += 1

    assert c == 7


def test_map_moving():
    t = Map.from_input(M)
    assert t.curr() == "."
    t.move()
    assert t.curr() == "."
    t.move()
    assert t.curr() == "#"
    t.move()
    assert t.curr() == "."
    t.move()
    assert t.curr() == "#"
