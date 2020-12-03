from dataclasses import dataclass
from typing import Any
import re


MOVE_COL = 3
MOVE_ROW = 1


@dataclass
class Trees:
    m: [str]
    pos: [int]

    def __init__(self, tree):
        self.m = tree
        self.pos = [0, 0]

    def at(self, pos: [int]) -> str:
        row, col = pos
        return self.m[row][col]

    def curr(self) -> str:
        return self.at(self.pos)

    def move(self, mr: int = MOVE_ROW, dx: int = MOVE_COL) -> bool:
        row, col = self.pos
        nr = row + mr
        if nr >= len(self.m):
            return False
        self.pos = [nr, (col + dx) % len(self.m[0])]
        return True

    def count(self, dy: int, dx: int) -> int:
        c = 0
        while self.move(dy, dx):
            c += int(self.curr() == "#")
        return c


def main():
    inputs = [str(s) for s in open("input.txt", "r").read().splitlines()]
    moves = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    a = 1
    [a := a * c for c in [Trees(inputs).count(*move) for move in moves]]
    print(a)


if __name__ == "__main__":
    main()
