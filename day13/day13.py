with open("input.txt") as f:
    DEPARTURE = int(f.readline().strip())
    IDS = [
        (pos, int(i))
        for pos, i in enumerate(f.readline().strip().split(","))
        if i != "x"
    ]


def part1():
    min_waiting_time, earliest_bus_id = 10 ** 10, -1
    for i in [i for pos, i in IDS]:
        remainder = DEPARTURE % i
        if remainder == 0 or (i - remainder) < min_waiting_time:
            min_waiting_time = i - remainder
            earliest_bus_id = i

    return min_waiting_time * earliest_bus_id


def part2():
    pass


print("Part 1", part1())
print("Part 2", part2())
