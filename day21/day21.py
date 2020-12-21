from collections import defaultdict

with open("input.txt") as f:
    foods_per_allergen = defaultdict(list)
    ingredients = []
    for ing, ale in [r.split("(") for r in f.readlines()]:
        for allergen in ale.strip()[:-1].replace(",", "").split(" ")[1:]:
            foods_per_allergen[allergen].append(set(ing.split()))
        ingredients += ing.split()


ingredient_candidates = {}
for a, lists in foods_per_allergen.items():
    while len(lists) > 1:
        lists.append(lists.pop() & lists.pop())
    ingredient_candidates[a] = lists.pop()

safe_ingredients = set(ingredients)
for possible_ingredients in ingredient_candidates.values():
    safe_ingredients -= possible_ingredients

unsafe_ingredients = {}
while ingredient_candidates:
    allergens_left = list(ingredient_candidates.keys())
    for allergen in allergens_left:
        ingredient_candidates[allergen] -= set(unsafe_ingredients.keys())
        if len(ingredient_candidates[allergen]) == 1:
            unsafe_ingredients[ingredient_candidates[allergen].pop()] = allergen
            del ingredient_candidates[allergen]


print("Part 1", sum(ingredients.count(n) for n in safe_ingredients))
sorted_unsafe_ingredients = sorted(unsafe_ingredients.items(), key=lambda p: p[1])
print("Part 2", ",".join(i for i, a in sorted_unsafe_ingredients))
