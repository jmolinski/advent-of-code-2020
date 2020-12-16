with open("input.txt") as f:
    rules_d, my_d, tickets_d = f.read().split("\n\n")
    rules = [l.split(": ") for l in rules_d.split("\n")]
    rules = {n: [r.split("-") for r in ranges.split("or")] for (n, ranges) in rules}
    rules = {n: [range(int(s), int(e) + 1) for (s, e) in r] for (n, r) in rules.items()}
    my_ticket = list(int(i) for i in my_d.split("\n")[1].split(","))
    tickets = [[int(i) for i in r.split(",")] for r in tickets_d.split("\n")[1:]]

all_rules = set()
for field_rules in rules.values():
    all_rules |= set(field_rules)

error_sum_ticket = [
    ([v for v in t if not any(v in r for r in all_rules)], t) for t in tickets
]
valid_tickets = [t for err, t in error_sum_ticket if not err]

transposed = [list() for _ in range(len(valid_tickets[0]))]
for t in valid_tickets:
    for i, v in enumerate(t):
        transposed[i].append(v)

# match all rows to fields (with duplicates)
# all values from a row must match field rules
possible_field_pos = {
    n: {
        i
        for i, row in enumerate(transposed)
        if all(any(v in range for range in ranges) for v in row)
    }
    for (n, ranges) in rules.items()
}

mapped_fields = {}
while possible_field_pos:
    certain_fields = {f for f in possible_field_pos if len(possible_field_pos[f]) == 1}
    f = certain_fields.pop()
    mapped_fields[f] = possible_field_pos[f].pop()
    del possible_field_pos[f]
    for (_, matches_for_field) in possible_field_pos.items():
        if mapped_fields[f] in matches_for_field:
            matches_for_field.remove(mapped_fields[f])

departure_check_val = 1
for field, index in mapped_fields.items():
    if "departure" in field:
        departure_check_val *= my_ticket[index]

print("Part 1", sum(sum(err) for err, _ in error_sum_ticket))
print("Part 2", departure_check_val)
