from functools import reduce as fold_left
import operator

REVERSE_DIR = {"top": "down", "down": "top", "left": "right", "right": "left"}
DIR_VECTOR = {"top": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def sum_vec(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def get_monster_body():
    monster_img = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    monster_parts = [
        (x, y)
        for x, row in enumerate(monster_img)
        for y, c in enumerate(row)
        if c == "#"
    ]
    zero_x, zero_y = monster_parts[0]
    monster_parts = [sum_vec(p, (-zero_x, -zero_y)) for p in monster_parts]
    # all coords of monster parts are relative to 'current' position
    return monster_parts


class Tile:
    def __init__(self, id, rows):
        self.id = id
        self.full = rows
        self.border = {
            "top": self.full[0],
            "down": self.full[-1],
            "left": "".join(r[0] for r in self.full),
            "right": "".join(r[-1] for r in self.full),
        }
        self.borders = set(self.border.values())

    @classmethod
    def from_raw(cls, raw_chunk):
        id = int(raw_chunk[0].split()[1][:-1])
        return cls(id, raw_chunk[1:])

    def __repr__(self):
        return "\n".join(self.full)

    def without_borders(self):
        return Tile(self.id, [row[1:-1] for row in self.full[1:-1]])

    def mirror(self):
        return Tile(self.id, [row[::-1] for row in self.full])

    def rotate(self):
        return Tile(self.id, list(map(lambda s: "".join(s), zip(*self.full)))).mirror()

    @staticmethod
    def get_tile_variants(tile):
        mirrored = tile.mirror()
        return {
            tile,
            tile.rotate(),
            tile.rotate().rotate(),
            tile.rotate().rotate().rotate(),
            mirrored,
            mirrored.rotate(),
            mirrored.rotate().rotate(),
            mirrored.rotate().rotate().rotate(),
        }

    def match_to_edge(self, tile):
        variants = self.get_tile_variants(tile)
        for edge in self.border:
            for variant in variants:
                if self.border[edge] == variant.border[REVERSE_DIR[edge]]:
                    return edge, variant

        raise ValueError("Tiles can't be matched")

    def count_monsters(self):
        monsters = 0
        monster_body = get_monster_body()
        rows, cols = len(self.full), len(self.full[0])
        for variant in self.get_tile_variants(self):
            all_coords = [(x, y) for x in range(rows) for y in range(cols)]
            for cx, cy in all_coords:
                maybe_body = [sum_vec((cx, cy), p) for p in monster_body]
                if all(0 <= x < rows and 0 <= y < cols for x, y in maybe_body):
                    monsters += all(variant.full[x][y] == "#" for x, y in maybe_body)

        return monsters

    def count_hashes(self):
        return sum(row.count("#") for row in self.full)


class Image:
    def __init__(self, tiles):
        self.tiles = {t.id: t for t in tiles}
        self.adjacent = {
            t.id: [
                o
                for o in self.tiles.values()
                if t != o and t.borders & (o.borders | o.mirror().rotate().borders)
            ]
            for t in self.tiles.values()
        }

    def corners(self):
        return {t for t, adj in self.adjacent.items() if len(adj) == 2}

    def form_image(self):
        corner_tile = self.tiles[self.corners().pop()]
        grid = {corner_tile: (0, 0)}

        to_place = [(corner_tile, t.id) for t in self.adjacent[corner_tile.id]]

        while to_place:
            parent, tile_id = to_place.pop()
            relative_pos, rotated_tile = parent.match_to_edge(self.tiles[tile_id])
            self.tiles[tile_id] = rotated_tile
            grid[rotated_tile] = sum_vec(grid[parent], DIR_VECTOR[relative_pos])

            for neighbor in self.adjacent[tile_id]:
                if self.tiles[neighbor.id] not in grid:
                    to_place.append((rotated_tile, neighbor.id))

        grid = {coord: tile for tile, coord in grid.items()}
        rows = []
        for x in sorted(set(x for x, y in grid)):
            row = [
                grid[(x, y)].without_borders().full
                for y in sorted(set(y for x, y in grid))
            ]
            rows.extend("".join(a) for a in zip(*row))

        return Tile(0, rows)


with open("input.txt") as f:
    img = Image(Tile.from_raw(ch.splitlines()) for ch in f.read().split("\n\n"))


print("Part 1", fold_left(operator.mul, img.corners()))

image = img.form_image()
monster = get_monster_body()

print("Part 2", image.count_hashes() - image.count_monsters() * len(monster))
