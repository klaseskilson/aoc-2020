from typing import Any
import re


def parse(inp: str) -> Any:
    # get limits
    # a, b = [int(s) for s in inp.split() if s.isdigit()]
    m = re.match(
        r"(?P<low>\d+)\-(?P<high>\d+) (?P<letter>\w{1}): (?P<pw>\w+)", inp
    ).groupdict()
    return {
        "letter": m["letter"],
        "pw": m["pw"],
        "low": int(m["low"]),
        "high": int(m["high"])
    }

def validate(parsed: Any) -> bool:
    if parsed['letter'] not in parsed['pw'] and parsed['low'] > 0:
        return False

    counts = {}
    for letter in parsed['pw']:
        counts[letter] = counts[letter] + 1 if letter in counts else 1

    c = counts[parsed['letter']]
    return c >= parsed['low'] and c <= parsed['high']

def main():
    print("ok")
    inputs = open('input.txt', 'r').read().splitlines()
    valid = [validate(parse(l)) for l in inputs]
    c = 0
    for v in valid:
        if v:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
