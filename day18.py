import re

ADD_PATTERN = re.compile(r"(\d+) \+ (\d+)")
PAREN_PATTERN = re.compile(r"\(([^()]+)\)")


def reader():
    with open("inputs/day18.txt", "r") as f:
        for line in f:
            yield line.strip()


def eval_flat_part1(s):
    parts = s.split()
    n = int(parts[0])

    i = 1
    while i < len(parts):
        op = parts[i]
        val = int(parts[i + 1])

        if op == "+":
            n += val
        elif op == "*":
            n *= val
        else:
            raise AssertionError(n, op, val)

        i += 2

    return n


def replace_add(match) -> str:
    return str(int(match[1]) + int(match[2]))


def eval_flat_part2(s):
    while ADD_PATTERN.search(s):
        s = ADD_PATTERN.sub(replace_add, s)

    parts = s.split()
    n = int(parts[0])

    i = 1
    while i < len(parts):
        op = parts[i]
        val = int(parts[i + 1])

        if op == "+":
            n += val
        elif op == "*":
            n *= val
        else:
            raise AssertionError(n, op, val)

        i += 2

    return n


def eval_parentheses_part1(match):
    return str(eval_flat_part1(match[1]))


def eval_parentheses_part2(match):
    return str(eval_flat_part2(match[1]))


def calculate(part):
    total = 0

    for line in reader():
        if part == 1:
            while PAREN_PATTERN.search(line):
                line = PAREN_PATTERN.sub(eval_parentheses_part1, line)

            total += eval_flat_part1(line)
        else:
            while PAREN_PATTERN.search(line):
                line = PAREN_PATTERN.sub(eval_parentheses_part2, line)

            total += eval_flat_part2(line)

    return total


def part1():
    return calculate(1)


def part2():
    return calculate(2)


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
