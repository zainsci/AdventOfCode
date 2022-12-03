#! /bin/python
from collections import defaultdict


def solve(data):
    with open("input") as f:
        data = f.read().split("\n")
    data = [x.split(" ") for x in data]

    first = {"A": "rock", "B": "paper", "C": "scissors"}

    my_score = 0
    for i in data:
        x, y = i

        if first[x] == "rock":
            total = 0

            if y == "X":
                total += 3
                total += 0
            if y == "Y":
                total += 1
                total += 3
            if y == "Z":
                total += 2
                total += 6
            my_score += total

        if first[x] == "paper":
            total = 0

            if y == "X":
                total += 1
                total += 0
            if y == "Y":
                total += 2
                total += 3
            if y == "Z":
                total += 3
                total += 6
            my_score += total

        if first[x] == "scissors":
            total = 0

            if y == "X":
                total += 2
                total += 0
            if y == "Y":
                total += 3
                total += 3
            if y == "Z":
                total += 1
                total += 6
            my_score += total

    return my_score


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
