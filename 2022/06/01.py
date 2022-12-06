#! /bin/python3
from collections import defaultdict


def solve(data):
    start = 0
    for i in range(len(data)):
        if i + 4 < len(data):
            new_set = set(data[i : i + 4])
            if (len(new_set)) == 4:
                start = i + 4
                break

    return start


def main():
    with open("input") as f:
        data = f.read()

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
