from typing import List

MAGIC = 2020


def scan2d(entries: List[int]) -> List[int]:
    for i in entries:
        for j in entries:
            if i + j == MAGIC:
                return [i, j]


def scan3d(entries: List[int]) -> List[int]:
    for i in entries:
        for j in entries:
            for k in entries:
                if i + j + k == MAGIC:
                    return [i, j, k]


def get_numbers(name: str) -> List[int]:
    inputs = open(name, "r")
    return list(map(int, inputs.read().splitlines()))


def main1():
    entries = get_numbers("input.txt")
    a, b = scan2d(entries)
    print(a * b)


def main2():
    entries = get_numbers("input.txt")
    a, b, c = scan3d(entries)
    print(a * b * c)


if __name__ == "__main__":
    main2()
