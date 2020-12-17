def reader():
    with open("inputs/day3.txt", "r") as f:
        return f.readlines()


def count_trees(right, down):
    lines = reader()

    count = 0
    x = 0
    for i in range(0, len(lines), down):
        line = lines[i].strip()
        if line[x] == "#":
            count += 1

        x += right
        x %= len(line)

    return count


def part1():
    return count_trees(3, 1)


def part2():
    trees = 1
    for t in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees *= count_trees(*t)

    return trees


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
