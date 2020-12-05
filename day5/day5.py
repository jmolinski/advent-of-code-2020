with open("input.txt") as f:
    bin_loc = [
        l.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        for l in f.readlines()
    ]

seat_ids = {int(loc[:7], 2) * 8 + int(loc[7:], 2) for loc in bin_loc}

my_seat = [
    s
    for s in set(range(1, max(seat_ids))) - seat_ids
    if (s - 1) in seat_ids and (s + 1) in seat_ids
][0]

print("Part 1", max(seat_ids))
print("Part 2", my_seat)
