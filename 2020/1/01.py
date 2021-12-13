from collections import defaultdict


def solve(data):
    for i in data:
        if 2020-i in data:
            return i, 2020-i


def main():
    with open("input") as f:
        data = [int(x) for x in f.read().strip().split("\n")]

        x, y = solve(data)
        print(x*y)


if __name__ == "__main__":
    main()
