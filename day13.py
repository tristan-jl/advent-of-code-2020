def reader1():
    with open("inputs/day13.txt", "r") as f:
        n = int(f.readline())
        ids = [int(i) for i in f.readline().split(",") if i != "x"]
        return (n, ids)


def reader2():
    with open("inputs/day13.txt", "r") as f:
        return [
            (int(s), i) for i, s in enumerate(f.readlines()[1].split(",")) if s != "x"
        ]


def part1():
    start, ids = reader1()

    leave = ids[0] * (start // ids[0] + 1)
    leave_id = ids[0]

    for id in ids[1:]:
        n = start // id
        depart_time = id * (n + 1)
        if depart_time < leave:
            leave = depart_time
            leave_id = id
    return leave_id * (leave - start)


def part2():
    ids = reader2()
    t = 0
    mult = ids[0][0]

    for bus, offset in ids[1:]:
        while (t + offset) % bus != 0:
            t += mult
        mult *= bus

    return t


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
