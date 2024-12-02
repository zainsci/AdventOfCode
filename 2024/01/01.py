#! /bin/python3
from collections import defaultdict


def solve(data):
    left = []
    right = []
    total = 0

    for i in data:
        nums = i.split("  ")
        left.append(int(nums[0]))
        right.append(int(nums[-1]))

    left.sort()
    right.sort()
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    return total


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
