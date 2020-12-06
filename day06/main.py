def count(s: str) -> int:
    uniq = set()
    for l in s.replace("\n", ""):
        uniq.add(l)
    return len(uniq)


def main():
    answers = [str(s) for s in open("input.txt", "r").read().split("\n\n")]
    groups = [count(s) for s in answers]
    print("part 1", sum(groups))


if __name__ == "__main__":
    main()
