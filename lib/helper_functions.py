#!/usr/bin/env python3
# =========== IMPORTS =========== #
import os


# ========== FUNCTIONS ========== #
def get_user_input(player: str) -> int:
    while True:
        print(f"It is player {player}'s turn!")
        user_input = input(" > ")

        try:
            if int(user_input) in range(1, 10):
                return int(user_input) - 1

        except ValueError:
            print("Please input a number between [1 - 9]!")


def print_game_board(game_board: list[str]) -> None:
    os.system('cls')
    print('╔═══╦═══╦═══╗')

    for y in range(3):
        for x in range(3):
            print(f'║ {game_board[y * 3 + x]}', end=' ' if x != 2 else ' ║\n')

        print('╠═══╬═══╬═══╣' if y != 2 else '╚═══╩═══╩═══╝')


def test_for_win(game_board: list[str]) -> bool:
    horizontal_line_win = test_for_horizontal_line_win(game_board)
    vertical_line_win = test_for_vertical_line_win(game_board)
    diagonal_line_win = test_for_diagonal_line_win(game_board)
    draw = test_for_draw(game_board)

    return horizontal_line_win or vertical_line_win or diagonal_line_win or draw


def test_for_horizontal_line_win(game_board: list[str]) -> bool:
    # Test for horizontal line win
    for y in range(3):
        line_content = [game_board[y * 3 + x] for x in range(3)]

        if len(set(line_content)) == 1:
            winner = list(set(line_content))[0]
            print_winner(winner, game_board)
            return True

    return False


def test_for_vertical_line_win(game_board: list[str]) -> bool:
    # Test for vertical line win
    for x in range(3):
        line_content = [game_board[y * 3 + x] for y in range(3)]

        if len(set(line_content)) == 1:
            winner = list(set(line_content))[0]
            print_winner(winner, game_board)
            return True

    return False


def test_for_diagonal_line_win(game_board: list[str]) -> bool:
    # Test for diagonal line win
    for i in [0, 2]:
        x_range = [abs(x - i) for x in range(3)]
        line_content = [game_board[y * 3 + x]
                        for x, y in zip(x_range, range(3))]

        if len(set(line_content)) == 1:
            winner = list(set(line_content))[0]
            print_winner(winner, game_board)
            return True

    return False


def test_for_draw(game_board: list[str]) -> bool:
    # Test for draw
    if len(set(game_board)) == 2:
        print("Its a draw!")
        return True

    return False


def ask_for_new_match() -> bool:
    return input("Again?\n (j/n) > ") == "j"


def print_winner(winner: str, game_board: list[str]) -> None:
    print_game_board(game_board)
    print(f"Player {winner} won!")
