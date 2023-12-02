#! /bin/python3
from collections import defaultdict


def solve(data):
    games = {}
    winner = []

    for i in range(len(data)):
        game, config = data[i].split(": ")

        game_id = game.split(" ")[-1]
        games[game_id] = [[], [], []]
        config = config.split(" ")

        for j in range(0, len(config), 2):
            color = config[j+1]\
                .replace(",", "")\
                .replace(";", "")

            if color == "red":
                games[game_id][0] .append(int(config[j]))
            if color == "green":
                games[game_id][1] .append(int(config[j]))
            if color == "blue":
                games[game_id][2] .append(int(config[j]))

        curr_game = games[game_id]
        if max(curr_game[0]) <= 12 \
            and max(curr_game[1]) <= 13 \
                and max(curr_game[2]) <= 14:
            winner.append(int(game_id))

    return sum(winner)


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")

        print(solve(data))


if __name__ == "__main__":
    main()
