with open("input.txt") as f:
    starting_numbers = list(map(int, f.read().split(",")))


def find_nth_number(n):
    when_said = dict((n, i) for (i, n) in enumerate(starting_numbers[:-1], start=1))
    last = starting_numbers[-1]
    age = len(starting_numbers) - when_said[last] if last in when_said else 0
    when_said[last] = len(when_said) + 1

    for i in range(len(starting_numbers) + 1, n + 1):
        last = age
        age = (i - when_said[last]) if last in when_said else 0
        when_said[last] = i

    return last


print("Part 1", find_nth_number(2020))
print("Part 2", find_nth_number(30000000))
