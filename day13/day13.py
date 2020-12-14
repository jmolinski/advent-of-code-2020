import math

with open("input.txt") as f:
    DEPARTURE = int(f.readline().strip())
    IDS = [(pos, int(i)) for pos, i in enumerate(f.readline().split(",")) if i != "x"]


def part1():
    min_waiting_time, earliest_bus_id = 10 ** 10, -1
    for i in [i for pos, i in IDS]:
        remainder = DEPARTURE % i
        if remainder == 0 or (i - remainder) < min_waiting_time:
            min_waiting_time = i - remainder
            earliest_bus_id = i

    return min_waiting_time * earliest_bus_id


def extended_euclid(x, y):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while y > 0:
        q, x, y = math.floor(x / y), y, x % y
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return x0, y0


def invmod(a, m):
    x, y = extended_euclid(a, m)
    return x % m


def chinese_remainder_gauss(n, a):
    result = 0
    n_product = 1
    for x in n:
        n_product *= x

    for ai, ni in zip(a, n):
        bi = n_product // ni
        result += ai * bi * invmod(bi, ni)

    return result % n_product


def part2():
    # x = ai (mod ni)

    n = [i for (pos, i) in IDS]
    a = [(i - (pos % i)) % i for (pos, i) in IDS]

    return chinese_remainder_gauss(n, a)


print("Part 1", part1())
print("Part 2", part2())
