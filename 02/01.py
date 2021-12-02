POSITION = 0
DEPTH = 0


with open("data", "r", encoding="utf-8") as f:
    data = f.read().split("\n")

    for i in data:
        command, unit = i.split(" ")

        if command == "forward":
            POSITION += int(unit)

        if command == "down":
            DEPTH += int(unit)

        if command == "up":
            DEPTH -= int(unit)


print(POSITION * DEPTH)
