#! /bin/python3
from collections import Counter


def solve(data):
    left = []
    right = []
    total = 0

    for i in data:
        j, k = i.split("  ")
        left.append(int(j))
        right.append(int(k))

    right_counter = dict(Counter(right))

    for i in range(len(left)):
        try:
            total += left[i] * right_counter[left[i]]
        except:
            pass

    return total


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
