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

    top_three = max(total_cals)
    for i in range(2):
        last_max = max(total_cals)
        total_cals.remove(last_max)
        new_max = max(total_cals)
        top_three += new_max

    return top_three


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
