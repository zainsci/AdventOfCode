position = 0
depth = 0


with open("data", "r", encoding="utf-8") as f:
    data = f.read().split("\n")

    for i in data:
        command, unit = i.split(" ")

        if command == "forward":
            position += int(unit)

        if command == "down":
            depth += int(unit)

        if command == "up":
            depth -= int(unit)


print(position * depth)
