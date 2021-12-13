from collections import defaultdict


def solve(data):
    count = 0

    for line in data:
        nums, letter, password = line.split(" ")
        low, high = map(int, nums.split("-"))
        letter = letter[0]

        if high >= password.count(letter) >= low:
            count += 1

    return count


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
