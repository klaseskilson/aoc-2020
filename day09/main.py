def test(l: [int], c: int) -> bool:
    for a in l:
        for b in l:
            if a + b == c:
                return True
    return False

def calc(inp: [int]) -> int:
    curr = inp[:25]
    rest = inp[25:]
    for i in rest:
        assert len(curr) == 25
        if not test(curr, i):
            return i
        curr.pop(0)
        curr.append(i)


def main():
    inp = open("input.txt", "r").read().splitlines()
    num = [int(n) for n in inp]
    p1 = calc(num)
    print("part 1", p1)

    ## part 2
    for w in range(2, len(num)):
        for i in range(len(num)):
            sub = num[i:i+w]
            len(sub)
            if sum(sub) == p1:
                print("part 2", min(sub), max(sub), min(sub) + max(sub), sub)


if __name__ == "__main__":
    main()
