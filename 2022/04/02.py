#! /bin/python3
from collections import defaultdict


def solve(data):
    total = 0
    for group in data:
        pair_a, pair_b = [x.split("-") for x in group.split(",")]

        min_a, max_a = int(pair_a[0]), int(pair_a[-1])
        min_b, max_b = int(pair_b[0]), int(pair_b[-1])

        if min_a >= min_b and max_a <= max_b:
            total += 1
            continue
        if min_b >= min_a and max_b <= max_a:
            total += 1
            continue

        if min_a >= min_b and min_a <= max_b:
            total += 1
        elif max_a >= min_b and max_a <= max_b:
            total += 1
        elif min_b >= min_a and min_b <= max_a:
            total += 1
        elif max_b >= min_a and max_b <= max_a:
            total += 1

    return total


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
