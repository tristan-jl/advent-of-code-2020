import re

FIELD_RE = re.compile(r"^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$")


def reader(valid_only=False):
    with open("inputs/day16.txt", "r") as f:
        rules, my_ticket, tickets = f.read().split("\n\n")

    rules_dict = dict()

    for line in rules.splitlines():
        m = FIELD_RE.match(line)
        rules_dict[m[1]] = (int(m[2]), int(m[3]), int(m[4]), int(m[5]))

    my_ticket_list = [int(i) for i in my_ticket.splitlines()[1].split(",")]

    def tickets_gen():
        for line in tickets.splitlines()[1:]:
            yield [int(i) for i in line.split(",")]

    def valid_tickets_gen():
        for line in tickets.splitlines()[1:]:
            ticket = [int(i) for i in line.split(",")]
            for n in ticket:
                for b1, e1, b2, e2 in rules_dict.values():
                    if b1 <= n <= e1 or b2 <= n <= e2:
                        break
                else:
                    break
            else:
                yield ticket

    if valid_only:
        return rules_dict, my_ticket_list, valid_tickets_gen

    return rules_dict, my_ticket_list, tickets_gen


def get_error_sum(rules, ticket):
    for n in ticket:
        for l1, u1, l2, u2 in rules.values():
            if l1 <= n <= u1 or l2 <= n <= u2:
                break
        else:
            return n
    else:
        return None


def part1():
    rules, _, tickets = reader()

    error_sum = 0
    for ticket in tickets():
        n = get_error_sum(rules, ticket)
        if n:
            error_sum += n

    return error_sum


def part2():
    rules, my_ticket, tickets = reader(valid_only=True)

    possible_positions = {
        pos: {
            k
            for k, (l1, u1, l2, u2) in rules.items()
            if all(
                l1 <= ticket[pos] <= u1 or l2 <= ticket[pos] <= u2
                for ticket in tickets()
            )
        }
        for pos in range(len(next(tickets())))
    }

    positions = dict()
    while possible_positions:
        for k, v in tuple(possible_positions.items()):
            if len(v) == 1:
                (key,) = v
                positions[key] = k
                possible_positions.pop(k)
                for v in possible_positions.values():
                    v.discard(key)

    result = 1
    for key, pos in positions.items():
        if key.startswith("departure "):
            result *= my_ticket[pos]

    return result


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
