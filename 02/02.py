POSITION = 0
DEPTH = 0
AIM = 0

with open("data", "r", encoding="utf-8") as f:
    data = f.read().split("\n")

    for i in data:
        command, unit = i.split(" ")

        if command == "forward":
            POSITION += int(unit)
            DEPTH += AIM*int(unit)

        if command == "down":
            AIM += int(unit)

        if command == "up":
            AIM -= int(unit)


print(POSITION * DEPTH)
