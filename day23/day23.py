with open("input.txt") as f:
    CIRCLE = list(int(c) for c in f.read())


def part1(circle):
    for i in range(100):
        picked = circle[1:4]
        circle[1:4] = []
        put_after = circle.index(
            (sorted(c for c in circle if c < circle[0]) or [max(circle)])[-1]
        )
        circle[put_after + 1 : put_after + 1] = picked
        circle.append(circle.pop(0))

    final = circle[circle.index(1) + 1 :] + circle[: circle.index(1)]
    return "".join(str(c) for c in final)


class Node:
    __slots__ = ["value", "next"]

    def __init__(self, value, previous):
        self.value = value
        if previous:
            previous.next = self
        self.next = None


def part2(circle):
    first = Node(circle[0], None)
    previous = first
    for v in circle[1:]:
        previous = Node(v, previous)

    for v in range(max(circle) + 1, 1000 * 1000 + 1):  # a million
        previous = Node(v, previous)

    # construct O(1) lookup table for nodes by their value
    current = first
    lookup_table = [None] * (1000 * 1000 + 1)
    while current:
        lookup_table[current.value] = current
        current = current.next

    previous.next = first
    current = first

    for _ in range(10 * 1000 * 1000):
        # cut 3 elements
        cut = current.next
        current.next = cut.next.next.next

        # find place to place
        excluded = (cut.value, cut.next.value, cut.next.next.value)
        put_after_value = current.value - 1
        while put_after_value in excluded or put_after_value == 0:
            if put_after_value == 0:
                put_after_value = 1000 * 1000
            else:
                put_after_value -= 1

        place_after = lookup_table[put_after_value]

        # put 3 elements in place
        cut.next.next.next, place_after.next = place_after.next, cut

        # advance current
        current = current.next

    while current.value != 1:
        current = current.next
    return current.next.value * current.next.next.value


print("Part 1", part1(CIRCLE[:]))
print("Part 2", part2(CIRCLE[:]))
