from collections import Counter


def reader():
    with open("inputs/day11.txt", "r") as f:
        return [list(s.strip()) for s in f]


def _index(lines, x, y) -> str:
    if y < 0:
        return " "
    elif y >= len(lines):
        return " "
    elif x < 0:
        return " "
    elif x >= len(lines[0]):
        return " "
    return lines[y][x]


def _adjacent(lines, i, j):
    def _inner():
        for _j in range(j - 1, j + 2):
            for _i in range(i - 1, i + 2):
                if (_i, _j) != (i, j):
                    yield _index(lines, _i, _j)

    return tuple(_inner())


def part1():
    previous_state = None
    seats = reader()

    while seats != previous_state:
        previous_state = seats

        new_lines = []
        for j, row in enumerate(seats):
            line_c = []
            for i, c in enumerate(row):
                if c == "L":
                    if _adjacent(seats, i, j).count("#") == 0:
                        line_c.append("#")
                    else:
                        line_c.append("L")
                elif c == "#":
                    if _adjacent(seats, i, j).count("#") >= 4:
                        line_c.append("L")
                    else:
                        line_c.append("#")
                else:
                    line_c.append(c)

            new_lines.append("".join(line_c))

        seats = tuple(new_lines)

    return sum(line.count("#") for line in seats)


def part2():
    previous_state = None
    seats = reader()

    while seats != previous_state:
        previous_state = seats

        d = Counter()
        for j, line in enumerate(seats):
            for i, c in enumerate(line):
                if c == "#":
                    for d_y, d_x in (
                        (0, 1),
                        (0, -1),
                        (1, 0),
                        (-1, 0),
                        (1, 1),
                        (-1, -1),
                        (1, -1),
                        (-1, 1),
                    ):
                        y_i, x_i = j + d_y, i + d_x
                        c = _index(seats, x_i, y_i)
                        while c not in "L# ":
                            y_i, x_i = y_i + d_y, x_i + d_x
                            c = _index(seats, x_i, y_i)
                        if c != " ":
                            d[(y_i, x_i)] += 1

        new_lines = []
        for j, line in enumerate(seats):
            line_c = []
            for i, c in enumerate(line):
                if c == "L":
                    if d[(j, i)] == 0:
                        line_c.append("#")
                    else:
                        line_c.append("L")
                elif c == "#":
                    if d[(j, i)] >= 5:
                        line_c.append("L")
                    else:
                        line_c.append("#")
                else:
                    line_c.append(c)

            new_lines.append("".join(line_c))

        seats = tuple(new_lines)

    return sum(line.count("#") for line in seats)


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
