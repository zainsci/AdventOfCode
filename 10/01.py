POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

BRACKETS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}


def get_point(line):
    stack = []
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]
    for i in range(len(line)):
        if line[i] in opening:
            stack.append(line[i])

        elif line[i] in closing:
            if stack[-1] == BRACKETS[line[i]]:
                stack.pop()
            else:
                return POINTS[line[i]]
    return 0


def count_points(data):
    total_points = 0

    for line in data:
        total_points += get_point(line)

    return total_points


with open("data") as f:
    data = f.read().splitlines()

    print(count_points(data))
