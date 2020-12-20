import numpy as np


def reader():
    with open("inputs/day12.txt", "r") as f:
        for line in f:
            yield (line[0], int(line[1:]))


def part1():
    coord = np.array([0, 0], dtype=int)
    direction = np.array([1, 0], dtype=int)

    for d, n in reader():
        if d == "N":
            coord[1] += n
        elif d == "S":
            coord[1] -= n
        elif d == "E":
            coord[0] += n
        elif d == "W":
            coord[0] -= n
        elif d == "F":
            coord += n * direction
        else:
            if d == "R":
                n *= -1
            n *= np.pi / 180
            direction = np.dot(
                np.array([[np.cos(n), -np.sin(n)], [np.sin(n), np.cos(n)]], dtype=int),
                direction,
            )

    return abs(coord[0]) + abs(coord[1])


def part2():
    coord = np.array([0, 0], dtype="int64")
    w_coord = np.array([10, 1], dtype="int64")

    def diff():
        return w_coord - coord

    for d, n in reader():
        if d == "N":
            w_coord[1] += n
        elif d == "S":
            w_coord[1] -= n
        elif d == "E":
            w_coord[0] += n
        elif d == "W":
            w_coord[0] -= n
        elif d == "F":
            d = diff()
            coord += n * d
            w_coord = coord + d
        else:
            if d == "R":
                n *= -1
            n *= np.pi / 180

            w_coord = coord + np.dot(
                np.array(
                    [[np.cos(n), -np.sin(n)], [np.sin(n), np.cos(n)]], dtype="int64"
                ),
                diff(),
            )

    return abs(coord[0]) + abs(coord[1])


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
