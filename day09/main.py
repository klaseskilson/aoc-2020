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
        print(i)
        assert len(curr) == 25
        if not test(curr, i):
            return i
        curr.pop(0)
        curr.append(i)


def main():
    inp = open("input.txt", "r").read().splitlines()
    num = [int(n) for n in inp]
    print("part 1", calc(num))

    # ## part 2
    # for i in range(len(instr)):
    #     cmd, _val = instr[i]
    #     cp = [ele[:] for ele in instr]
    #     if cmd == 'nop':
    #         cp[i][0] = 'jmp'
    #     elif cmd == 'jmp':
    #         cp[i][0] = 'nop'
    #     f, s = calc(cp)
    #     if s:
    #         print("part 2", f, s, i, cmd)
    #         break


if __name__ == "__main__":
    main()
