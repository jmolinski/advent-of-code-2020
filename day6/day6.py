from string import ascii_lowercase
from collections import Counter

with open("input.txt") as f:
    raw_input = f.read()

group_choices_and_size = [
    (Counter(c for c in group if c in ascii_lowercase), group.count("\n") + 1)
    for group in raw_input.split("\n\n")
]

print("Part 1", sum(len(g) for (g, _) in group_choices_and_size))
print("Part 2", sum(list(g.values()).count(s) for (g, s) in group_choices_and_size))
