def calc(inp: [[str, int]]) -> int:
    acc = 0
    i = 0
    seen = []
    while True:
        if i in seen:
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
    print("part 1", calc(instr))

if __name__ == "__main__":
    main()
