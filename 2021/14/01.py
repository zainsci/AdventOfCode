from collections import defaultdict, Counter


def solve(template, data, times):
    data = [x.split(" -> ") for x in data.split("\n")]

    for i in range(times):
        match = ""
        for x in range(len(template)-1):
            for y in data:
                if y[0] == template[x:x+2]:
                    match += f"{template[x]}{y[1]}"
        template = match+template[-1]

    most_commons = list(Counter(template).values())
    most_commons.sort()
    return most_commons[0], most_commons[-1]


def main():
    with open("input") as f:
        template, data = f.read().strip().split("\n\n")

        a, b = solve(template, data, 10)
        print(b-a)


if __name__ == "__main__":
    main()
