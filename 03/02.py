def get_rating(data, gas):
    ratings = data

    for i in range(len(data[0])):
        new_arr = []
        ones = 0
        zeros = 0

        if len(ratings) == 1:
            continue

        for arr in ratings:
            arr = list(arr)

            if arr[i] == "1":
                ones += 1
            if arr[i] == "0":
                zeros += 1

        if ones == zeros:
            if gas == "o":
                for arr in ratings:
                    if arr[i] == "1":
                        new_arr.append(arr)
            else:
                for arr in ratings:
                    if arr[i] == "0":
                        new_arr.append(arr)

        if gas == "o":
            if ones > zeros:
                for arr in ratings:
                    if arr[i] == "1":
                        new_arr.append(arr)
            if ones < zeros:
                for arr in ratings:
                    if arr[i] == "0":
                        new_arr.append(arr)

        else:
            if ones > zeros:
                for arr in ratings:
                    if arr[i] == "0":
                        new_arr.append(arr)
            if ones < zeros:
                for arr in ratings:
                    if arr[i] == "1":
                        new_arr.append(arr)

        ratings = new_arr

    return ratings[0]


with open("data", "r") as f:
    data = f.read().split()

    oxygen_rating = get_rating(data, "o")
    co2_rating = get_rating(data, "co2")

    print(int(oxygen_rating, 2) * int(co2_rating, 2))
