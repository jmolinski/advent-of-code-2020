from collections import defaultdict

with open("input.txt") as f:
    paths = []
    for line in map(lambda s: list(s.strip()), f.readlines()):
        path = []
        while line:
            d = line.pop(0)
            if d in "sn":
                d += line.pop(0)
            path.append(d)
        paths.append(path)

DIRECTIONS = {
    "ne": (1, -1, 0),
    "e": (1, 0, -1),
    "se": (0, 1, -1),
    "sw": (-1, 1, 0),
    "w": (-1, 0, 1),
    "nw": (0, -1, 1),
}


def add_vec(v1, v2):
    return tuple(a + b for a, b in zip(v1, v2))


black_tiles = set()
for path in paths:
    position = (0, 0, 0)
    for d in path:
        position = add_vec(position, DIRECTIONS[d])

    if position in black_tiles:
        black_tiles.remove(position)
    else:
        black_tiles.add(position)

part1_black_tiles = set(black_tiles)
for i in range(100):
    black_neighbors = defaultdict(int)
    for t in black_tiles:
        for vec_d in DIRECTIONS.values():
            black_neighbors[add_vec(t, vec_d)] += 1

    black_to_white = {
        t for t in black_tiles if black_neighbors[t] == 0 or black_neighbors[t] > 2
    }
    white_to_black = {
        t for t, n in black_neighbors.items() if t not in black_tiles and n == 2
    }
    black_tiles = (black_tiles - black_to_white) | white_to_black

print("Part 1", len(part1_black_tiles))
print("Part 2", len(black_tiles))
