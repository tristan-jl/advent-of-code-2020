from typing import FrozenSet, NamedTuple


class Food(NamedTuple):
    ingredients: FrozenSet[str]
    allergens: FrozenSet[str]


def reader():
    with open("inputs/day21.txt", "r") as f:
        for line in f:
            ingredient_raw, _, allergens_raw = line.partition("(contains ")
            yield Food(
                frozenset(ingredient_raw.strip().split()),
                frozenset(allergens_raw.strip(")\n").split(", ")),
            )


def get_ingredient_allergens():
    potential_allergens = {}
    for food in reader():
        for allergen in food.allergens:
            if allergen not in potential_allergens:
                potential_allergens[allergen] = set(food.ingredients)

            potential_allergens[allergen] &= food.ingredients

    assigned = {}
    while potential_allergens:
        for k, v in tuple(potential_allergens.items()):
            if len(v) == 1:
                (value,) = v
                assigned[k] = value

                for v in potential_allergens.values():
                    v.discard(value)

                del potential_allergens[k]

    return assigned


def part1():
    assigned = get_ingredient_allergens()

    total = 0
    known = set(assigned.values())
    for food in reader():
        total += len(food.ingredients - known)

    return total


def part2():
    assigned = get_ingredient_allergens()

    items = sorted(assigned.items())
    return ",".join(val for _, val in items)


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
