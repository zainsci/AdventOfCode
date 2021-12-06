from collections import defaultdict


def count_fish(data, days):
    total_count = defaultdict(int)

    for i in data:
        total_count[i] += 1

    for i in range(days):
        temp_count = defaultdict(int)

        for fish, count in total_count.items():
            if fish == 0:
                temp_count[6] += count
                temp_count[8] += count
            else:
                temp_count[fish-1] += count

        total_count = temp_count

    return sum(total_count.values())


with open("data", "r") as f:
    data = [int(x) for x in f.read().split(",")]

    print(count_fish(data, 80))  # Part 01
    print(count_fish(data, 256))  # Part 02
