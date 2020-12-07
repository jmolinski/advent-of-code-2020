with open("input.txt") as f:
    req = {}
    for line in f.readlines():
        name = " ".join(line.split(" ", maxsplit=2)[:2])
        if "no other" in line:
            req[name] = {}
        else:
            bag_req = [
                s.strip().split(" ")
                for s in line.replace(".", "").split("contain")[1].split(",")
            ]
            req[name] = {(na + " " + nb): int(count) for count, na, nb, _ in bag_req}


def expand_tree(name):
    s = set(req[name])
    for child in req[name].keys():
        s |= expand_tree(child)
    return s


def total_bags(name):
    cost = 0
    for child, multiplier in req[name].items():
        cost += multiplier + multiplier * total_bags(child)
    return cost


expanded_req = {key: expand_tree(key) for key in req}
part1 = sum("shiny gold" != key and "shiny gold" in expanded_req[key] for key in req)

print("Part 1", part1)
print("Part 2", total_bags("shiny gold"))
