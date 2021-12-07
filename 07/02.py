from collections import defaultdict


def count_fuel(data):
    fuel_count = defaultdict(int)

    for i in range(round(max(data)/2)):
        count = 0
        for p in data:
            unit = sum([x for x in range(1, abs(p-i)+1)])
            count += unit

        fuel_count[i] = count

    return min(fuel_count.values())


with open("data", "r")as f:
    data = [int(x) for x in f.read().split(",")]

    print(count_fuel(data))
