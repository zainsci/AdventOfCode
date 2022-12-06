#! /bin/python3
from collections import defaultdict


def solve(data):
    stacks, steps = data[0], data[1]
    stacks = stacks.split("\n")
    steps = steps.split("\n")

    # [Z] [M] [P]
    # 012345678910
    cargo = {x: [] for x in stacks[-1].strip().split("   ")}
    stacks = stacks[:-1][::-1]

    for floor in stacks:
        cols = len(floor) // 4
        idx = -3
        for col in range(1, cols + 2):
            idx += 4
            curr_crate = floor[idx]
            if curr_crate == " ":
                continue
            cargo[str(col)].append(curr_crate)

    parsed_steps = []
    for step in steps:
        step = step.split(" ")
        parsed_steps.append((step[1], step[3], step[5]))

    for step in parsed_steps:
        crate, first, second = step
        crate = int(crate)

        for i in range(crate):
            dummy = cargo[first].pop()
            cargo[second].append(dummy)

    end_phrase = ""
    for key, value in cargo.items():
        end_phrase += value[-1]

    return end_phrase


def main():
    with open("input") as f:
        data = f.read().split("\n\n")

        sol = solve(data)
        print(sol)


if __name__ == "__main__":
    main()
