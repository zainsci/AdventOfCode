#! /bin/python
from collections import defaultdict


def solve(data):
    with open("input") as f:
        data = f.read().split("\n\n")
    data = [x.split("\n") for x in data]

    total_cals = []

    for i in data:
        total = sum([int(x) for x in i])
        total_cals.append(total)
    return max(total_cals)


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
