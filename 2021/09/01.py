def find_risk(data):
    matrix = data
    for dx in range(len(matrix)):
        matrix[dx].insert(0, 10)
        matrix[dx].append(10)
    extra = [10 for i in range(len(matrix[0]))]
    matrix.insert(0, extra)
    matrix.append(extra)

    risk = []

    for dx in range(1, len(data)-1):
        for dy in range(1, len(data[0])-1):
            adjacent = [
                matrix[dx][dy-1],
                matrix[dx][dy+1],
                matrix[dx-1][dy],
                matrix[dx+1][dy],
            ]
            if matrix[dx][dy] < min(adjacent):
                risk.append(matrix[dx][dy]+1)
    return sum(risk)


with open("data") as f:
    data = [[int(y) for y in x] for x in f.read().split("\n")]

    risk = find_risk(data)
    print(risk)
