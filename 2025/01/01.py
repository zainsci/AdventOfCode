#! /bin/python3
from collections import defaultdict


def solve(data):
    code = 50
    count = 0

    for seq in data:
        if seq[0] == "L":
            code = (code - int(seq[1:])) % 100
        elif seq[0] == "R":
            code = (code + int(seq[1:])) % 100

        if code == 0:
            count += 1

    return count


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
