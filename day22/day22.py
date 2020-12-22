with open("input.txt") as f:
    p1, p2 = f.read().split("\n\n")
    p1_cards = [int(c) for c in p1.split("\n")[1:]]
    p2_cards = [int(c) for c in p2.split("\n")[1:]]


def part1(deck1, deck2):
    while deck1 and deck2:
        p1, p2 = deck1.pop(0), deck2.pop(0)
        if p1 > p2:
            deck1.extend([p1, p2])
        else:
            deck2.extend([p2, p1])

    return deck1, deck2


def play_recursive(deck1, deck2):
    history1, history2 = set(), set()
    while deck1 and deck2:
        if tuple(deck1) in history1 or tuple(deck2) in history2:
            return deck1, []

        history1.add(tuple(deck1))
        history2.add(tuple(deck2))

        p1, p2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= p1 and len(deck2) >= p2:
            result = play_recursive(deck1[:p1], deck2[:p2])
            if result[0]:
                deck1.extend([p1, p2])
            else:
                deck2.extend([p2, p1])
        else:
            if p1 > p2:
                deck1.extend([p1, p2])
            else:
                deck2.extend([p2, p1])

    return deck1, deck2


def score_winner(d1, d2):
    return sum(i * c for i, c in enumerate(d1[::-1] or d2[::-1], start=1))


print("Part 1", score_winner(*part1(p1_cards[:], p2_cards[:])))
print("Part 2", score_winner(*play_recursive(p1_cards[:], p2_cards[:])))
