import itertools


def part1(sum_amount):
    seen = set()

    with open("inputs/day1.txt", "r") as f:
        for line in f.readlines():
            num = int(line)

            if 2020 - num in seen:
                return num * (2020 - num)

            seen.add(num)

        else:
            raise NotImplementedError("Cannot find sum pair.")


def part2(sum_amount):
    with open("inputs/day1.txt", "r") as f:
        nums = [int(line) for line in f.readlines()]

    for a, b, c in itertools.combinations(nums, 3):
        if a + b + c == 2020:
            return a * b * c

    else:
        raise NotImplementedError("Cannot find sum triplet.")


def main():
    print("part 1: ", part1(2020))
    print("part 2: ", part2(2020))


if __name__ == "__main__":
    main()
