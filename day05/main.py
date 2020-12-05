from math import floor, ceil


def from_bin(s: str, z: str, o: str) -> int:
    return int(s.replace(z, "0").replace(o, "1"), 2)


def get_seat(boarding_pass: str) -> int:
    row = from_bin(boarding_pass[:7], z="F", o="B")
    col = from_bin(boarding_pass[7:], z="L", o="R")
    return row * 8 + col


def main():
    boardings = [str(s) for s in open("input.txt", "r").read().splitlines()]
    seats = [get_seat(str(s)) for s in boardings]
    print("part 1", max(seats))

    seats.sort()
    i = 8
    for seat in seats[8:-7]:
        # print(i, seat, seats[i + 1], seat + 1)
        # if seats[i + 1] != seat + 1:
        if seat + 1 not in seats:
            print("omg", seat)
        i += 1


if __name__ == "__main__":
    main()
