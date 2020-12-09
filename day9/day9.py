with open("input.txt") as f:
    codes = list(map(int, f.readlines()))


def part1():
    possible_summands = codes[:25]

    def is_sum(n):
        for k in possible_summands:
            diff = n - k
            if diff * 2 != n and diff in possible_summands:
                return True

    for i in range(25, len(codes)):
        if not is_sum(codes[i]):
            return codes[i]

        possible_summands.pop(0)
        possible_summands.append(codes[i])


def part2(val):
    sum = codes[0] + codes[1]
    oldest, newest = 0, 1

    while not (sum == val and newest - oldest > 1):
        while sum < val:
            newest += 1
            sum += codes[newest]
        while sum > val:
            sum -= codes[oldest]
            oldest += 1

    return min(codes[oldest : newest + 1]) + max(codes[oldest : newest + 1])


part1_val = part1()
print("Part 1", part1_val)
print("Part 2", part2(part1_val))
