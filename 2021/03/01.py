gamma = ""
epsilon = ""


with open("data", "r") as f:
    data = f.read().split()
    bits = {}
    for i in range(len(data[0])):
        bits[f"0{i}"] = 0
        bits[f"1{i}"] = 0

    for arr in data:
        arr = list(arr)

        for i in range(len(arr)):
            if arr[i] == "1":
                bits[f"1{i}"] += 1
            if arr[i] == "0":
                bits[f"0{i}"] += 1
    for i in range(len(data[0])):
        if bits[f"0{i}"] > bits[f"1{i}"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    print(int(gamma, 2) * int(epsilon, 2))
