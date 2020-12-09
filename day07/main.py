from typing import Dict, Any
from collections import ChainMap


def clean(s: str) -> str:
    alpha = "".join([l for l in s if l.isalpha()])
    if not alpha[-1] == "s":
        alpha += "s"
    return alpha


def rule(r: str) -> Dict[str, Any]:
    container, inner = r.split(" contain")
    return { clean(container): [clean(i) for i in inner.split(",")] }


def rules(r: [str]) -> Dict[str, Any]:
    return dict(ChainMap(*[rule(i) for i in r]))


def search(d: Dict[str, Any], s: Any) -> bool:
    if type(s) == str:
        if "shinygoldbags" == s:
            return True
        if s not in d:
            return False
        return search(d, d[s])
    return True in [search(d, i) for i in s]


def count(d: Dict[str, Any]) -> int:
    c = 0
    for v in d.values():
        c += search(d, v)
    return c

def main():
    input = open("input.txt", "r").read().splitlines()
    bags = rules(input)
    breakpoint()
    print("part 1", count(bags))


if __name__ == "__main__":
    main()
