from collections import defaultdict, deque
from tqdm import tqdm


def reader():
    with open("inputs/day15.txt", "r") as f:
        for num in f.read().split(","):
            yield int(num)


def calculate(max_turn):
    seen = defaultdict(lambda: deque(maxlen=2))

    for i, n in enumerate(reader()):
        seen[n].append(i)

    for turn in tqdm(range(len(seen), max_turn)):
        if len(seen[n]) == 1:
            n = 0
        else:
            n = seen[n][-1] - seen[n][0]

        seen[n].append(turn)

    return n


def part1():
    return calculate(2020)


def part2():
    return calculate(30_000_000)


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
