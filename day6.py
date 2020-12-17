def reader():
    with open("inputs/day6.txt", "r") as f:
        for item in f.read().split("\n\n"):
            yield item.splitlines()


def part1():
    count = 0

    for group in reader():
        s = set(group.pop())
        for i in group:
            s = s.union(set(i))

        count += len(s)

    return count


def part2():
    count = 0

    for group in reader():
        s = set(group.pop())
        for i in group:
            s = s.intersection(set(i))

        count += len(s)

    return count


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
