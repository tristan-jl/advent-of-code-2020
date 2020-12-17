def reader():
    with open("inputs/day5.txt", "r") as f:
        for line in f.readlines():
            line = line.replace("F", "0").replace("B", "1")
            line = line.replace("R", "1").replace("L", "0")
            yield int(line, 2)


def part1():
    current_max = 0
    for seat_id in reader():
        current_max = max(current_max, seat_id)

    return current_max


def part2():
    possible_seats = set(range(1024))

    for seat_id in reader():
        possible_seats.remove(seat_id)

    for seat in possible_seats:
        if seat + 1 not in possible_seats and seat - 1 not in possible_seats:
            return seat


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
