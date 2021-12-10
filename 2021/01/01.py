count = 0
prev = 0

with open("data", "r", encoding="utf-8") as f:
    data = f.read().split()
    prev = data[0]

    for n in data:
        if n == prev:
            print(n, "N/A")

        if int(n) > int(prev):
            print(n, "(+++++)")
            prev = n
            count += 1

        if int(n) < int(prev):
            print(n, "(-----)")
            prev = n

print(count)
