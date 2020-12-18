def reader():
    code = []
    with open("inputs/day8.txt", "r") as f:
        for line in f.readlines():
            op, n = line.split()
            n = int(n)
            code.append((op, n))

        return code


def run(code, flip=-1):
    swap = {"jmp": "nop", "nop": "jmp"}

    visited = set()
    acc = 0
    line = 0
    while line not in visited and line < len(code):
        visited.add(line)
        op, n = code[line]

        if line == flip:
            op = swap[op]

        if op == "acc":
            acc += n
            line += 1
        elif op == "jmp":
            line += n
        elif op == "nop":
            line += 1
        else:
            raise NotImplementedError(op)

    if line == len(code):
        return acc, visited
    else:
        raise RuntimeError(acc, visited, "Already visited")


def part1():
    code = reader()
    try:
        (acc,) = run(code)
    except RuntimeError as e:
        (
            acc,
            _,
            _,
        ) = e.args

    return acc


def part2():
    code = reader()

    try:
        _, visited = run(code)
    except RuntimeError as e:
        (
            _,
            visited,
            _,
        ) = e.args
    else:
        ValueError

    for line in visited:
        if code[line][0] in {"nop", "jmp"}:
            try:
                acc, _ = run(code, line)
                return acc
            except RuntimeError:
                pass


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
