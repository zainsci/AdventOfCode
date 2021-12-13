def fill_hashes(arr_1, arr_2):
    for x in range(len(arr_1)):
        for y in range(len(arr_1[0])):
            if arr_2[x][y] == "#":
                arr_1[x][y] = "#"
    return arr_1


def fold_along(axis, num, paper):
    if axis == "x":
        arr_1 = [x[:num] for x in paper]
        arr_2 = [x[num+1:][::-1] for x in paper]

        return fill_hashes(arr_1, arr_2)

    if axis == "y":
        arr_1, arr_2 = paper[:num], paper[num+1:][::-1]

        return fill_hashes(arr_1, arr_2)


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

    for i in folds:
        paper = fold_along(i[0], int(i[1]), paper)
    for i in paper:
        print(i)
