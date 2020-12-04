import re

FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate(passport: str) -> bool:
    missing = [f for f in FIELDS if f not in passport]
    return len(missing) == 0


def year(passport: str, key: str, limits: [int]) -> bool:
    m = re.search(f"{key}:(\d+)", passport)
    return m is not None and (int(m.group(1)) >= limits[0] and int(m.group(1)) <= limits[1])

def p(a):
    print(a)
    return None

def moar_validate(passport: str) -> bool:
    if not year(passport, "byr", [1920, 2002]):
        p("byr")
        return False
    if not year(passport, "iyr", [2010, 2020]):
        p("iyr")
        return False
    if not year(passport, "eyr", [2020, 2030]):
        p("eyr")
        return False
    cm = re.search(r"hgt:(\d+)cm", passport)
    inch = re.search(r"hgt:(\d+)in", passport)
    if not cm and not inch:
        p("hgt")
        return False
    if cm and not (int(cm.group(1)) >= 150 and int(cm.group(1)) <= 193):
        p("cm")
        return False
    if inch and not (int(inch.group(1)) >= 59 and int(inch.group(1)) <= 76):
        p("in")
        return False
    hair = re.search(r"hcl:#[a-f0-9]{6}", passport)
    if not hair:
        p("hair")
        return False
    eye = re.search(r"ecl:(\w)", passport)
    if not eye or eye.group(1) not in 'amb blu brn gry grn hzl oth':
        p("eye")
        return False
    nr = re.search(r"pid:\d{9}", passport)
    if not nr:
        p("nr")
        return False
    return True


def main():
    inputs = [str(s) for s in open("input.txt", "r").read().split("\n\n")]
    valid = [p for p in inputs if validate(p)]
    print("valid, part 1: ", len(valid))

    moar_valid = [p for p in inputs if moar_validate(p)]
    print("valid, part 2: ", len(moar_valid))


if __name__ == "__main__":
    main()
