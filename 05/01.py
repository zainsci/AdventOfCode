from collections import defaultdict


def count_plus(data):
    index = defaultdict(int)

    for line in data:
        x1, y1, x2, y2 = line
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    index[(x, y)] += 1

    return index


def count_cross(data):
    index = count_plus(data)
    for line in data:
        x1, y1, x2, y2 = line
        dx = 1 if x2 >= x1 else -1
        dy = 1 if y2 >= y1 else -1

        if abs(x2-x1) == abs(y2-y1):
            y = y1
            for x in range(x1, x2+dx, dx):
                index[y, x] += 1
            y += dy
    return index


def count_highest(arr):
    count = 0
    for i in arr:
        if arr[i] > 1:
            count += 1
    return count


with open("data", "r") as f:
    data = [

        [int(x) for x in i.split(",")]

        for i in f.read().replace(" -> ", ",").split("\n")

    ]

    part01 = count_highest(count_plus(data))
    part02 = count_highest(count_cross(data))
    print(part01)
    print(part02)
