#! /bin/python3
from collections import defaultdict


def solve(data):
    nums = ""
    out = []

    for line in data:
        for char in line:
            try:
                if int(char):
                    nums += char

            except Exception:
                pass
        out.append(int(nums[0]+nums[-1]))
        nums = ""

    return sum(out)


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
