def fill_hashes(arr_1, arr_2):
    for x in range(len(arr_1)):
        for y in range(len(arr_1[0])):
            if arr_2[x][y] == "#":
                arr_1[x][y] = "#"
    return arr_1


def count_hashes(arr):
    count = 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == "#":
                count += 1
    return count


def fold_along(axis, num, paper):
    count = 0

    if axis == "x":
        arr_1 = [x[:num] for x in paper]
        arr_2 = [x[num+1:][::-1] for x in paper]

        arr_1 = fill_hashes(arr_1, arr_2)
        count += count_hashes(arr_1)

    if axis == "y":
        arr_1, arr_2 = paper[:num], paper[num+1:][::-1]

        arr_1 = fill_hashes(arr_1, arr_2)
        count += count_hashes(arr_1)

    return count


with open("input") as f:
    data = f.read()
    axis, folds = data.split("\n\n")
    axis = [list(map(int, x.split(","))) for x in axis.split("\n")]
    folds = [x.replace("fold along ", "").split("=")
             for x in folds.split("\n")]

    x_max = max([x[0] for x in axis])
    y_max = max([x[1] for x in axis])

    paper = [["." for x in range(x_max+1)] for y in range(y_max+1)]

    for x, y in axis:
        paper[y][x] = "#"

    print(fold_along(folds[0][0], int(folds[0][1]), paper))
