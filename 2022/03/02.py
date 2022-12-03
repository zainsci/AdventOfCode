#! /bin/python3
from collections import defaultdict


def solve(data):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lower = {key: value + 1 for value, key in enumerate(alpha)}
    upper = {key: value + 27 for value, key in enumerate(alpha.upper())}
    priority = lower | upper

    unique = []
    for i in range(0, len(data), 3):
        group = data[i : i + 3]
        a, b, c = set(group[0]), set(group[1]), set(group[2])
        inter = a.intersection(b)
        inter = inter.intersection(c)
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
