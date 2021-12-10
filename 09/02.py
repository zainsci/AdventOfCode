from collections import deque

# Didn't solved all by myself
# took a little help from
# https://youtu.be/rWUFJ0yIDGo


def find_basins(data):
    VISITED = set()
    basins = []

    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) not in VISITED and data[i][j] != 9:
                size = 0
                Q = deque()
                Q.append((i, j))

                while Q:
                    (i, j) = Q.popleft()
                    if (i, j) in VISITED:
                        continue
                    VISITED.add((i, j))
                    size += 1

                    for d in range(4):
                        r = i+DR[d]
                        c = j+DC[d]

                        if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] != 9:
                            Q.append((r, c))
                basins.append(size)

    return basins


with open("data") as f:
    data = [[int(y) for y in x] for x in f.read().split("\n")]

    basins = find_basins(data)
    basins.sort()
    print(basins[-1]*basins[-2]*basins[-3])
