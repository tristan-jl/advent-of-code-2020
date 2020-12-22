from collections import defaultdict
from typing import NamedTuple, Tuple
import re

PATTERN = re.compile(r"^mem\[(\d+)\] = (\d+)")


def reader():
    with open("inputs/day14.txt", "r") as f:
        for line in f:
            d = dict()
            if line.startswith("mask"):
                _, _, mask_s = line.partition(" = ")
                d["mask"] = (
                    int(mask_s.replace("X", "0"), 2),
                    int(mask_s.replace("X", "1"), 2),
                )
                yield d
            else:
                match = PATTERN.match(line)
                d["mem"] = (int(match[1]), int(match[2]))
                yield d


def part1():
    memory = defaultdict(int)
    mask_or, mask_and = (0, -1)
    for d in reader():
        if "mask" in d:
            mask_or, mask_and = d["mask"]
        else:
            target, number = d["mem"]
            masked = (number | mask_or) & mask_and
            memory[target] = masked

    return sum(memory.values())


class Mask(NamedTuple):
    ones_mask: int
    x_masks: Tuple[Tuple[int, int], ...]

    def targets(self, number):
        number = number | self.ones_mask
        for x_mask_or, x_mask_and in self.x_masks:
            yield (number | x_mask_or) & x_mask_and


def parse_mask(s: str) -> Mask:
    one_mask = int(s.replace("X", "0"), 2)
    xs = [match.start() for match in re.finditer("X", s)]
    x_masks = []
    for i in range(1 << len(xs)):
        number_or = 0
        number_and = -1
        for j in range(len(xs)):
            bit = (i & (1 << j)) >> j
            if bit:
                number_or |= 1 << (len(s) - 1 - xs[j])
            else:
                number_and &= ~(1 << (len(s) - 1 - xs[j]))
        x_masks.append((number_or, number_and))
    return Mask(one_mask, tuple(x_masks))


def reader2():
    with open("inputs/day14.txt", "r") as f:
        for line in f:
            d = dict()
            if line.startswith("mask"):
                _, _, mask_s = line.partition(" = ")
                d["mask"] = parse_mask(mask_s)
                yield d
            else:
                match = PATTERN.match(line)
                d["mem"] = (int(match[1]), int(match[2]))
                yield d


def part2():
    memory = defaultdict(int)

    mask = Mask(-1, ())
    for d in reader2():
        if "mask" in d:
            mask = d["mask"]
        else:
            target, number = d["mem"]

            for target in mask.targets(target):
                memory[target] = number

    return sum(memory.values())


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
