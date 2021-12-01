COUNT = 0
PREV = 1000

with open("data", "r", encoding="utf-8") as f:
    data = f.read().split()

    for i in range(len(data)):
        if i-2 >= 0:
            num = int(data[i-2]) + int(data[i-1]) + int(data[i])

            if num > int(PREV):
                print(num, "(+++++)")
                PREV = num
                COUNT += 1

            if num < int(PREV):
                print(num, "(-----)")
                PREV = num

print(COUNT)
