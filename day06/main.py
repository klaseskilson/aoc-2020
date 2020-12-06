def count(s: str) -> int:
    return len(set(s.replace("\n", "")))


def count_unified(s: str) -> int:
    return len(set(s[0]).intersection(*[set(s) for s in s[1:]]))


def main():
    answers = open("input.txt", "r").read().split("\n\n")
    print("part 1", sum([count(s) for s in answers]))
    print("part 2", sum([count_unified(s.split('\n')) for s in answers]))


if __name__ == "__main__":
    main()
