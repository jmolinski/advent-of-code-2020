with open("input.txt") as f:
    instructions = [(lambda l: (l[0], int(l[1:])))(l) for l in f.readlines()]

N, S, E, W = (1, 0), (-1, 0), (0, 1), (0, -1)
ROTATE_LEFT = {N: W, W: S, S: E, E: N}
ROTATE_RIGHT = {v: k for k, v in ROTATE_LEFT.items()}


def rotate_90d(v, cwise):
    rotators = {False: lambda p: (p[1], -p[0]), True: lambda p: (-p[1], p[0])}
    return rotators[cwise](v)


def mul_vec(v, m):
    return v[0] * m, v[1] * m


def add_vec(v, m):
    return v[0] + m[0], v[1] + m[1]


def part1():
    direction, pos = E, (0, 0)

    for key, value in instructions:
        if key in "RL":
            for _ in range(value // 90):
                direction = {"R": ROTATE_RIGHT, "L": ROTATE_LEFT}[key][direction]
        elif key in "NSEW":
            pos = add_vec(mul_vec({"N": N, "E": E, "W": W, "S": S}[key], value), pos)
        else:
            pos = add_vec(mul_vec(direction, value), pos)

    return abs(pos[0]) + abs(pos[1])


def part2():
    pos, waypoint = (0, 0), add_vec(mul_vec(E, 10), N)

    for key, value in instructions:
        if key in "RL":
            relative_pos = add_vec(waypoint, mul_vec(pos, -1))
            for _ in range(value // 90):
                relative_pos = rotate_90d(relative_pos, key == "R")
            waypoint = add_vec(pos, relative_pos)
        elif key in "NSEW":
            waypoint = add_vec(
                mul_vec({"N": N, "E": E, "W": W, "S": S}[key], value), waypoint
            )
        else:
            relative_pos = add_vec(mul_vec(pos, -1), waypoint)
            pos = add_vec(pos, mul_vec(relative_pos, value))
            waypoint = add_vec(waypoint, mul_vec(relative_pos, value))

    return abs(pos[0]) + abs(pos[1])


print("Part 1", part1())
print("Part 2", part2())
