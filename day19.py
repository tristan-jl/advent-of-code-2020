import re


def reader():
    with open("inputs/day19.txt", "r") as f:
        rules_string, lines_string = f.read().split("\n\n")

        rules = dict()
        for line in rules_string.splitlines():
            k, v = line.split(": ")
            rules[k] = v

        lines = lines_string.splitlines()

        return rules, lines


def get_re(rules, n):
    def build_re(k):
        rule_i = rules[k]

        if rule_i.startswith('"'):
            return rule_i.strip('"')
        else:
            parts = rule_i.split()
            inner_part = "".join(
                "|" if part == "|" else build_re(part) for part in parts
            )
            return f"({inner_part})"

    return re.compile(build_re(n))


def part1():
    rules, lines = reader()
    pattern_0 = get_re(rules, "0")

    count = 0
    for line in lines:
        if pattern_0.fullmatch(line):
            count += 1

    return count


def part2() -> int:
    rules_s, lines = reader()

    def _get_re(s: str) -> str:
        if s == "|":
            return s

        rule_s = rules_s[s]
        if rule_s.startswith('"'):
            return rule_s.strip('"')
        else:
            return f'({"".join(_get_re(part) for part in rule_s.split())})'

    re_42 = re.compile(_get_re("42"))
    re_31 = re.compile(_get_re("31"))

    count = 0
    for line in lines:
        pos = 0

        count_42 = 0
        while match := re_42.match(line, pos):
            count_42 += 1
            pos = match.end()

        count_31 = 0
        while match := re_31.match(line, pos):
            count_31 += 1
            pos = match.end()

        if 0 < count_31 < count_42 and pos == len(line):
            count += 1

    return count


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
