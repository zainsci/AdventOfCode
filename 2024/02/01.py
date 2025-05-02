#! /bin/python3
from collections import defaultdict


def is_strictly_ascending(nums):
    return all(nums[i] < nums[i+1] for i in range(len(nums)-1))


def is_strictly_descending(nums):
    return all(nums[i] > nums[i+1] for i in range(len(nums)-1))


def check_levels_diff(nums):
    return all(abs(nums[i] - nums[i+1]) <= 3 for i in range(len(nums)-1))


def solve(data):
    count = 0

    for row in data:
        nums = [int(x) for x in row.split(" ")]

        if is_strictly_ascending(nums) and check_levels_diff(nums):
            count += 1
            continue

        elif is_strictly_descending(nums) and check_levels_diff(nums):
            count += 1
            continue

    return count


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
