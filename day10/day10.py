with open("input.txt") as f:
    adapters = sorted(map(int, f.readlines()))


def part1():
    diffs = [b - a for a, b in zip(adapters, adapters[1:])]
    return (diffs.count(1) + 1) * (diffs.count(3) + 1)


def part2():
    paths = {a: 0 for a in adapters}
    paths[max(adapters)] = 1
    paths[0] = 0

    for a in adapters[::-1]:
        for diff in (1, 2, 3):
            k = a - diff
            if k in paths:
                paths[k] += paths[a]

    return paths[0]


print("Part 1", part1())
print("Part 2", part2())
