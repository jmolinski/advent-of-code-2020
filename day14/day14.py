import re
from collections import defaultdict

with open("input.txt") as f:
    data_chunks = []

    chunk = []
    for line in f.readlines():
        if "mask" in line:
            if chunk:
                data_chunks.append(chunk)
            chunk = [[], []]
            chunk[0] = list(enumerate(line.split("= ")[1].strip()[::-1]))
        else:
            pos, val = re.findall(r"\d+", line)
            chunk[1].append((int(pos), int(val)))

    data_chunks.append(chunk)


def apply_mask_part1(mask, val):
    for p, bit in mask:
        if bit == '0':
            val &= ~(1 << p)
        if bit == '1':
            val |= 1 << p

    return val


def part1():
    mem = defaultdict(int)

    for mask, instructions in data_chunks:
        for pos, val in instructions:
            mem[pos] = apply_mask_part1(mask, val)

    return sum(mem.values())


def apply_mask_part2(mask, val):
    for p, bit in mask:
        if bit == '1':
            val |= 1 << p

    return make_all_possible_values([m for m in mask if m[1] == 'X'], val)


def make_all_possible_values(mask, val):
    stack = [(mask, val)]
    res = []
    while stack:
        m, v = stack.pop()
        pos, bit = m.pop()
        v0 = apply_mask_part1([(pos, '0')], v)
        v1 = apply_mask_part1([(pos, '1')], v)
        if m:
            stack.extend([(m[:], v0), (m[:], v1)])
        else:
            res.extend([v0, v1])

    return res


def part2():
    mem = defaultdict(int)

    for mask, instructions in data_chunks:
        for pos, val in instructions:
            for masked_pos in apply_mask_part2(mask[::], pos):
                mem[masked_pos] = val

    return sum(mem.values())


print('Part 1', part1())
print('Part 2', part2())
