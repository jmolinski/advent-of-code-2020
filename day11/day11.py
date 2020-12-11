with open("input.txt") as f:
    MATRIX = [list(row.strip()) for row in f.readlines()]


WIDTH, HEIGHT = len(MATRIX[0]), len(MATRIX)
MOVEMENT_VECTORS = [
    (a, b) for a in range(-1, 2) for b in range(-1, 2) if not (a == 0 and b == 0)
]


def within_board(h, w):
    return 0 <= h < HEIGHT and 0 <= w < WIDTH


def count_adjacent(board, h, w):
    count = 0

    for dh, dw in MOVEMENT_VECTORS:
        nh, nw = h + dh, w + dw
        if within_board(nh, nw) and board[h + dh][w + dw] == "#":
            count += 1

    return count


def count_first_in_line(board, h, w):
    count = 0

    for dh, dw in MOVEMENT_VECTORS:
        nh, nw = h + dh, w + dw
        while True:
            if not within_board(nh, nw) or board[nh][nw] == "L":
                break
            if board[nh][nw] == "#":
                count += 1
                break
            nh, nw = nh + dh, nw + dw

    return count


def run_round(previous_state, neighbor_counter, empty_threshold):
    new_state = [[""] * WIDTH for _ in range(HEIGHT)]

    for h in range(HEIGHT):
        for w in range(WIDTH):
            this_field = previous_state[h][w]
            occupied_nei = neighbor_counter(previous_state, h, w)

            if this_field == "L" and occupied_nei == 0:
                new_state[h][w] = "#"
            elif this_field == "#" and occupied_nei >= empty_threshold:
                new_state[h][w] = "L"
            else:
                new_state[h][w] = this_field

    return new_state


def run_simulation(part):
    neighbor_counter = count_adjacent if part == 1 else count_first_in_line
    empty_threshold = 4 if part == 1 else 5
    previous, current = MATRIX, run_round(MATRIX, neighbor_counter, empty_threshold)

    while previous != current:
        previous, current = current, run_round(
            current, neighbor_counter, empty_threshold
        )

    return sum(row.count("#") for row in current)


print("Part 1", run_simulation(part=1))
print("Part 2", run_simulation(part=2))
