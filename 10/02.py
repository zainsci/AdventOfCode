POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

BRACKETS = {
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
}


def get_lines(line):
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
                return 0

    return stack


def count_points(data):
    incomplete_lines = []
    for line in data:
        incomplete_lines.append(get_lines(line))
    incomplete_lines = list(filter(lambda x: x != 0, incomplete_lines))

    scores = []
    for line in incomplete_lines:
        count = 0
        line = line[::-1]
        for b in line:
            count *= 5
            count += POINTS[BRACKETS[b]]
        scores.append(count)

    scores.sort()
    return scores[round(len(scores)/2)]


with open("data") as f:
    data = f.read().splitlines()

    print(count_points(data))
