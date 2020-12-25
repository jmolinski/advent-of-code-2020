with open("input.txt") as f:
    card_public, door_public = int(f.readline()), int(f.readline())

mod = 20201227


def find_loop_count(n, subject):
    value = 1
    for i in range(n * subject):
        if value == n:
            return i

        value = (value * subject) % mod


print("Part 1", pow(card_public, find_loop_count(door_public, 7), mod))
