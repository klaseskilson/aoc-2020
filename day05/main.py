from math import floor, ceil


def search(instr: str, ranges: [int]) -> int:
    lo, hi = ranges
    for r in instr:
        d = hi - lo
        if r in "BR":
            lo = ceil(lo + (d / 2))
        else:
            hi = floor(hi - (d / 2))
    return lo


def get_seat(boarding_pass: str) -> int:
    row = search(boarding_pass[:6], [0, 127])
    col = search(boarding_pass[7:], [0, 7])
    return row * 8 + col


def main():
    seats = [get_seat(str(s)) for s in open("input.txt", "r").read().splitlines()]
    print("part 1", max(seats))

    seats.sort()
    potential =  seats[8:-8]
    i = 8
    for seat in potential:
        print(i, seat, seats[i+1], seats[i+1] - seat)
        if seats[i+1] - seat == 2:
            print("omg", seat)
        i+=1


if __name__ == "__main__":
    main()
