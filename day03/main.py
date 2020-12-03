from dataclasses import dataclass
from typing import Any
import re


MOVE_COL = 3
MOVE_ROW = 1


@dataclass
class Map:
    m: [str]
    pos: [int]

    def __init__(self, tree):
        self.m = tree
        self.pos = [0, 0]

    @classmethod
    def from_input(cls, inpu: bytearray):
        return cls([str(s) for s in inpu.splitlines()])

    def at(self, pos: [int]) -> str:
        row, col = pos
        return self.m[row][col]

    def curr(self) -> str:
        return self.at(self.pos)

    def move(self, mr: int = MOVE_ROW, mc: int = MOVE_COL) -> bool:
        row, col = self.pos
        nr = row + mr
        nc = col + mc
        if nr >= len(self.m):
            return False
        if nc >= len(self.m[0]):
            nc = nc % len(self.m[0])
        self.pos = [nr, nc]
        return True

    def size(self) -> [int]:
        return [len(self.m), len(self.m[0])]

    def p(self) -> str:
        return "\n".join(self.m)


def main():
    inputs = open("input.txt", "r").read()
    m = [[1,1], [1,3], [1, 5], [1, 7], [2, 1]]
    a = 1

    for move in m:
        trees = Map.from_input(inputs)
        c = 0
        while trees.move(*move):
            if trees.curr() == "#":
                c += 1
        a *= c
        print(c)
        print(a)

    print(c)


if __name__ == "__main__":
    main()
