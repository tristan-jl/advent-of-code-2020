import collections
import functools


def reader():
    with open("inputs/day10.txt", "r") as f:
        return sorted([int(n) for n in f])


def part1():
    current_output = 0
    counts = {1: 0, 2: 0, 3: 1}

    for num in reader():
        counts[num - current_output] += 1
        current_output = num

    return counts[1] * counts[3]


@functools.lru_cache(maxsize=None)
def combinations(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return combinations(n - 1) + combinations(n - 2) + combinations(n - 3)


def part2():
    nums = reader()
    c = collections.defaultdict(int, {0: 1})

    for n in nums:
        c[n] = c[n - 1] + c[n - 2] + c[n - 3]

    return c[nums[-1]]


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
