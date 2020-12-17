from collections import defaultdict

with open("input.txt") as f:
    initial_active_2d = set()
    for i, row in enumerate(f.readlines()):
        for j, c in enumerate(row.strip()):
            if c == "#":
                initial_active_2d.add((i, j))


def get_neighbors(i, *rest, acc=None):
    acc = acc or {tuple()}
    acc = {(*a, i + di) for a in acc for di in (-1, 0, 1)}
    return get_neighbors(*rest, acc=acc) if rest else acc


def run_simulation(active):
    for _ in range(6):
        active_neighbors = defaultdict(int)
        for a in active:
            for nei in get_neighbors(*a) - {a}:
                active_neighbors[nei] += 1
        active = {a for a in active if active_neighbors[a] in (2, 3)} | {
            n for n in active_neighbors if active_neighbors[n] == 3
        }

    return len(active)


print("Part 1", run_simulation([(*a, 0) for a in initial_active_2d]))
print("Part 2", run_simulation([(*a, 0, 0) for a in initial_active_2d]))
