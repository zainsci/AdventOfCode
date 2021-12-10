import re
import numpy as np


def check_if_won(board):
    board = np.array(board)

    winner_list = ["X", "X", "X", "X", "X"]
    cols = [
        [x for x in range(0, 25, 5)],
        [x for x in range(1, 25, 5)],
        [x for x in range(2, 25, 5)],
        [x for x in range(3, 25, 5)],
        [x for x in range(4, 25, 5)],
    ]

    # Check Rows
    if np.array_equal(winner_list, board[0:5]):
        return True
    if np.array_equal(winner_list, board[5:10]):
        return True
    if np.array_equal(winner_list, board[10:15]):
        return True
    if np.array_equal(winner_list, board[15:20]):
        return True
    if np.array_equal(winner_list, board[20:25]):
        return True

    # Check Cols
    if np.array_equal(winner_list, board[cols[0]]):
        return True
    if np.array_equal(winner_list, board[cols[1]]):
        return True
    if np.array_equal(winner_list, board[cols[2]]):
        return True
    if np.array_equal(winner_list, board[cols[3]]):
        return True
    if np.array_equal(winner_list, board[cols[4]]):
        return True


def find_winner(seq, data):
    for num in seq:
        for i in range(len(data)):
            data[i] = ["X" if x == num else x for x in data[i]]
            if check_if_won(data[i]):

                return num, data[i]


def find_last_winner(seq, data):
    winners = [None for i in data]
    total_boards = len(data)

    for num in seq:
        for i in range(len(data)):
            data[i] = ["X" if x == num else x for x in data[i]]

            if check_if_won(data[i]) and not winners[i]:
                winners[i] = "X"

                if len([i for i in winners if i == "X"]) == total_boards:
                    return num, data[i]


def get_unmarked(board):
    total = 0
    for i in board:
        try:
            total += int(i)
        except ValueError:
            pass
    return total


with open("data", "r") as f:
    data = f.read().split("\n\n")
    sequence = data[0].split(",")
    boards = np.array([
        re.split(" +", board.replace("\n", " ").strip())
        for board in data[1:]
    ])

    winner_num, winner_board = find_winner(sequence, boards)
    winner_total_unmarked = get_unmarked(winner_board)

    print(int(winner_num) * winner_total_unmarked)

    last_num, last_board = find_last_winner(sequence, boards)
    last_total_unmarked = get_unmarked(last_board)
    print(int(last_num) * last_total_unmarked)
