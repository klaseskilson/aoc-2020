def calc(inp: [[str, int]]) -> [int, bool]:
    acc = 0
    i = 0
    seen = []
    while True:
        if i in seen or i == len(inp):
            break
        seen.append(i)
        inst, val = inp[i]
        if inst == 'nop':
            i += 1
            next
        elif inst == 'acc':
            i += 1
            acc += val
            next
        elif inst == 'jmp':
            i += val
            next
    return [acc, i == len(inp)]


def main():
    inp = open("input.txt", "r").read().splitlines()
    instr = [[a.split(' ')[0], int(a.split(' ')[1])] for a in inp]
    final, success = calc(instr)
    print("part 1", final, success)

    ## part 2
    for i in range(len(instr)):
        cmd, _val = instr[i]
        cp = [ele[:] for ele in instr]
        if cmd == 'nop':
            cp[i][0] = 'jmp'
        elif cmd == 'jmp':
            cp[i][0] = 'nop'
        f, s = calc(cp)
        if s:
            print("part 2", f, s, i, cmd)
            break


if __name__ == "__main__":
    main()
