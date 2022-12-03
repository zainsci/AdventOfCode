#! /bin/python3
from collections import defaultdict


def solve(data):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lower = {key: value + 1 for value, key in enumerate(alpha)}
    upper = {key: value + 27 for value, key in enumerate(alpha.upper())}
    priority = lower | upper

    unique = []
    for sack in data:
        first, second = sack[: len(sack) // 2], sack[len(sack) // 2 :]
        first = set(first)
        second = set(second)
        inter = first.intersection(second)
        unique.append(list(inter)[0])

    sum = 0
    for i in unique:
        sum += priority[i]

    return sum


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
