with open("data", "r") as f:
    data = [x.split(" | ") for x in f.read().split("\n")]

    count = 0
    for i in data:
        count += len([
            x for x in i[-1].split(" ")
            if len(x) in [2, 3, 4, 7]
        ])

    print(count)
