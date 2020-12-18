import itertools
import re


def reader():
    with open("inputs/day2.txt", "r") as f:
        for line in f.readlines():
            m = re.match(
                r"^(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>\w):\s(?P<password>\w+)$", line
            )
            if m:
                yield m.groupdict()
            else:
                raise ValueError(f"Could not match {line}")


def part1():
    count = 0

    for d in reader():
        letter_count = d["password"].count(d["letter"])
        if int(d["min"]) <= letter_count and letter_count <= int(d["max"]):
            count += 1

    return count


def part2():
    count = 0

    for d in reader():
        contains_min = d["password"][int(d["min"]) - 1] == d["letter"]
        contains_max = d["password"][int(d["max"]) - 1] == d["letter"]
        if contains_min ^ contains_max:
            count += 1

    return count


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
