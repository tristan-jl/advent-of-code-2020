from collections import Counter


def reader(dims):
    active_cubes = set()

    with open("inputs/day17.txt", "r") as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line):
                if c == "#":
                    if dims == 3:
                        active_cubes.add((x, y, 0))
                    elif dims == 4:
                        active_cubes.add((x, y, 0, 0))
                    else:
                        raise TypeError

    return active_cubes


def part1():
    active_cubes = reader(3)
    neighbours = (-1, 0, 1)

    for _ in range(6):
        surroundings = Counter()

        for cube in active_cubes:
            for x_i in neighbours:
                for y_i in neighbours:
                    for z_i in neighbours:
                        if not x_i == y_i == z_i == 0:
                            surroundings[
                                (cube[0] + x_i, cube[1] + y_i, cube[2] + z_i)
                            ] += 1

        new_active_cubes = set()
        for k, v in surroundings.items():
            if v == 3:
                new_active_cubes.add(k)

        for cube in active_cubes:
            if surroundings[cube] in {2, 3}:
                new_active_cubes.add(cube)

        active_cubes = new_active_cubes

    return len(active_cubes)


def part2():
    active_cubes = reader(4)
    neighbours = (-1, 0, 1)

    for _ in range(6):
        surroundings = Counter()

        for cube in active_cubes:
            for x_i in neighbours:
                for y_i in neighbours:
                    for z_i in neighbours:
                        for w_i in neighbours:
                            if not x_i == y_i == z_i == w_i == 0:
                                surroundings[
                                    (cube[0] + x_i, cube[1] + y_i, cube[2] + z_i, cube[3] + w_i)
                                ] += 1

        new_active_cubes = set()
        for k, v in surroundings.items():
            if v == 3:
                new_active_cubes.add(k)

        for cube in active_cubes:
            if surroundings[cube] in {2, 3}:
                new_active_cubes.add(cube)

        active_cubes = new_active_cubes

    return len(active_cubes)


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
