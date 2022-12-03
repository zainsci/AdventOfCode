#! /bin/python
from collections import defaultdict


def solve(data):
    with open("input") as f:
        data = f.read().split("\n")
    data = [x.split(" ") for x in data]

    first = {"A": "rock", "B": "paper", "C": "scissors"}
    second = {"X": "rock", "Y": "paper", "Z": "scissors"}
    second_score = {"X": 1, "Y": 2, "Z": 3}

    my_score = 0
    for i in data:
        x, y = i

        if first[x] == second[y]:
            total = 3 + second_score[y]
            my_score += total
            continue

        if second[y] == "rock":
            total = 1
            if first[x] == "scissors":
                my_score += 6

            my_score += total

        if second[y] == "paper":
            total = 2
            if first[x] == "rock":
                total += 6

            my_score += total

        if second[y] == "scissors":
            total = 3
            if first[x] == "paper":
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
