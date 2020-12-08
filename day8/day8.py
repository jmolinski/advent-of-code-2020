with open("input.txt") as f:
    instructions = [(lambda i: [i[0], int(i[1])])(l.split()) for l in f.readlines()]


def run_instructions():
    acc, pos = 0, 0
    used = set()

    while True:
        if pos in used:
            return "part1", acc
        if pos == len(instructions):
            return "part2", acc

        used.add(pos)

        cmd, vec = instructions[pos]
        if cmd == "jmp":
            pos += vec
        elif cmd == "nop":
            pos += 1
        elif cmd == "acc":
            acc += vec
            pos += 1


def part2_try_substitutions():
    indices = [i for i, instr in enumerate(instructions) if instr[0] in ("jmp", "nop")]

    subst = {"nop": "jmp", "jmp": "nop"}
    for i in indices:
        instructions[i][0] = subst[instructions[i][0]]
        res = run_instructions()
        if res[0] == "part2":
            return res[1]
        instructions[i][0] = subst[instructions[i][0]]


print("Part 1", run_instructions()[1])
print("Part 2", part2_try_substitutions())
