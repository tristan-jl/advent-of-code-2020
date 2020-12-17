import re

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def part1():
    count = 0

    with open("inputs/day4.txt", "r") as f:
        text = f.read()

        for item in text.split("\n\n"):
            has_fields = True
            for field in fields - {"cid"}:
                match = re.search(r"(?<=" + field + r":)\S+", item)
                if not match:
                    has_fields = False
                    break

            if has_fields:
                count += 1

    return count


def part2():
    count = 0

    with open("inputs/day4.txt", "r") as f:
        text = f.read()

        for item in text.split("\n\n"):
            d = dict()

            for field in fields - {"cid"}:
                match = re.search(r"(?<=" + field + r":)\S+", item)
                if match:
                    d[field] = match.group(0)
                else:
                    d = None
                    break
            if d:
                m = re.match(r"^(\d+)(cm|in)$", d["hgt"])
                if m:
                    if (
                        (1920 <= int(d["byr"]) <= 2002)
                        and (2010 <= int(d["iyr"]) <= 2020)
                        and (2020 <= int(d["eyr"]) <= 2030)
                        and (
                            m[2] == "cm" and 150 <= int(m[1]) <= 193
                            or m[2] == "in" and 59 <= int(m[1]) <= 76
                        )
                        and re.match("^#[a-f0-9]{6}$", d["hcl"])
                        and d["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
                        and re.match("^[0-9]{9}$", d["pid"])
                    ):
                        count += 1

    return count


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
