def count(trees: [str], dy: int, dx: int) -> int:
    c, x, y = [0, 0, 0]
    while y < len(trees):
        c += trees[y][x % len(trees[0])] == "#"
        x += dx
        y += dy
    return c


def main():
    inputs = [str(s) for s in open("input.txt", "r").read().splitlines()]
    print("part one:", count(inputs, 1, 3))

    # part 2
    moves = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    a = 1
    [a := a * c for c in [count(inputs, *move) for move in moves]]
    print("part two:", a)


if __name__ == "__main__":
    main()
