from collections import defaultdict


def solve(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i, j, k


def main():
    with open("input") as f:
        data = [int(x) for x in f.read().strip().split("\n")]

        x, y, z = solve(data)
        print(x*y*z)


if __name__ == "__main__":
    main()
