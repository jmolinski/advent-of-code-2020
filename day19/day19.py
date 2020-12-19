import re

with open("input.txt") as f:
    rules_r, msgs_r = f.read().split("\n\n")
    messages = msgs_r.strip().splitlines()

    rules = {
        int(k): (
            r[1:-1] if '"' in r else [[int(v) for v in p.split()] for p in r.split("|")]
        )
        for k, r in [r.split(": ") for r in rules_r.strip().splitlines()]
    }


def expand_rule(num):
    if isinstance(rules[num], str):
        return {rules[num]}

    res = set()
    for case in rules[num]:
        res |= chain_substituted_values(*[expand_rule(r) for r in case])

    return res


def chain_substituted_values(head, *tail):
    if not tail:
        return head

    substituted_tail = chain_substituted_values(*tail)
    res = set()
    for v in head:
        for t in substituted_tail:
            res.add(v + t)

    return res


""" part 2
0: 8 11
8: 42 | 42 8  # can repeat 42 any number of times
11: 42 31 | 42 11 31  # can extend 42 42 ... 31 31 to any depth
"""

re_42, re_31 = f'({"|".join(expand_rule(42))})', f'({"|".join(expand_rule(31))})'
part2_rules = [  # rule 11 is limited to recursive depth 5
    f"^{re_42}+{p_11}$"
    for p_11 in {f"{re_42}{{{s}}}{re_31}{{{s}}}" for s in range(1, 6)}
]
print("Part 1", len(set(expand_rule(0)) & set(messages)))
print(
    "Part 2",
    sum(any(re.match(p, m) for p in part2_rules) for m in messages),
)
