def reader(batch_size=25):
    batch = []
    with open("inputs/day9.txt", "r") as f:
        for line in f:
            if len(batch) < batch_size + 1:
                batch.append(int(line))
                continue
            else:
                yield batch
                batch.pop(0)
                batch.append(int(line))


def read_all_nums():
    with open("inputs/day9.txt", "r") as f:
        return [int(i) for i in f.readlines()]


def find_num(batch_size=25):
    for batch in reader(batch_size):
        adds_up = False

        target = batch[-1]
        seen = set()
        for num in batch[:-1]:
            if target - num in seen:
                adds_up = True
                break
            else:
                seen.add(num)

        if not adds_up:
            return target
    else:
        raise NotImplementedError("All numbers add up")


def part1():
    return find_num()


def part2():
    target = find_num()
    nums = read_all_nums()
    start_index = 0
    end_index = 1
    current_sum = nums[start_index] + nums[end_index]

    while end_index < len(nums):
        if current_sum == target:
            sum_nums = nums[start_index : end_index + 1]
            return min(sum_nums) + max(sum_nums)
        elif current_sum < target:
            end_index += 1
            current_sum += nums[end_index]
        else:
            current_sum -= nums[start_index]
            start_index += 1

    raise NotImplementedError("Cannot find set")


def main():
    print("part 1: ", part1())
    print("part 2: ", part2())


if __name__ == "__main__":
    main()
