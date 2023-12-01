#! /bin/python3
from collections import defaultdict


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solve(data):
    digs = []
    out = []

    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            try:
                int(line[j])
                digs.append(line[j])
                continue
            except Exception:
                pass

            first = line[j:j+3]
            second = line[j:j+4]
            third = line[j:j+5]
            try:
                digs.append(digits[first])
            except Exception:
                pass
            try:
                digs.append(digits[second])
            except Exception:
                pass
            try:
                digs.append(digits[third])
            except Exception:
                pass

        out.append(int(digs[0]+digs[-1]))
        digs = []

    return sum(out)


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
