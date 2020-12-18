import re

LINE_PATTERN = re.compile("^([^ ]+ [^ ]+) bags contain (.*)$")
BAG_PATTERN = re.compile(r"(\d+) ([^ ]+ [^ ]+)")


def reader():
    with open("inputs/day7.txt", "r") as f:
        for line in f.readlines():
            d = dict()
            match = LINE_PATTERN.match(line)
            d["parent"] = match[1]
            d["bags"] = [
                (int(n), bag_type) for n, bag_type in BAG_PATTERN.findall(match[2])
            ]
            yield d


def part1():
    held_by = dict()

    for d in reader():
        for _, bag_type in d["bags"]:
            if bag_type in held_by:
                held_by[bag_type].append(d["parent"])
            else:
                held_by[bag_type] = [d["parent"]]

    found = set()
    todo = held_by["shiny gold"]

    while todo:
        colour = todo.pop()
        if colour not in found:
            found.add(colour)
            todo += held_by.get(colour, [])

    return len(found)


def part2():
    colours = dict()

    for d in reader():
        colours[d["parent"]] = d["bags"]

    total = -1
    todo = [(1, "shiny gold")]

    while todo:
        n, colour = todo.pop()
        total += n
        for n_i, colour_i in colours[colour]:
            todo.append((n * n_i, colour_i))

    return total


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
