COUNT = 0
PREV = 0

with open("data", "r", encoding="utf-8") as f:
    data = f.read().split()
    PREV = data[0]

    for n in data:
        if n == PREV:
            print(n, "N/A")

        if int(n) > int(PREV):
            print(n, "(+++++)")
            PREV = n
            COUNT += 1

        if int(n) < int(PREV):
            print(n, "(-----)")
            PREV = n

print(COUNT)
