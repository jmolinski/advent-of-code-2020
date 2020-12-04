with open("input.txt") as f:
    raw_input = f.read()

passports = [
    dict(map(lambda p: p.split(":"), map(str.strip, p.replace("\n", " ").split())))
    for p in raw_input.split("\n\n")
]

needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_p1 = [p for p in passports if needed_keys & set(p.keys()) == needed_keys]
print("Part 1", len(valid_p1))


def is_valid_data_piece(key, v):
    validators = {
        "byr": lambda k: 1920 <= int(k) <= 2002,
        "iyr": lambda k: 2010 <= int(k) <= 2020,
        "eyr": lambda k: 2020 <= int(k) <= 2030,
        "hgt": lambda k: int(k[:-2])
        in {"in": range(59, 77), "cm": range(150, 194)}[k[-2:]],
        "hcl": lambda k: len(k) == 7 and k[0] == "#" and int(k[1:], 16),
        "ecl": lambda k: k in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda k: len(k) == 9 and int(k),
    }
    try:
        return key not in validators or validators[key](v)
    except:
        return False


valid_p2 = sum(all(is_valid_data_piece(k, v) for k, v in p.items()) for p in valid_p1)
print("Part 2", valid_p2)
