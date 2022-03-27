#!/usr/bin/env python3
# =========== IMPORTS =========== #
from itertools import cycle
from random import shuffle
from tictactoe.lib.helper_functions import get_user_input, print_game_board, test_for_win, ask_for_new_match


# ========== FUNCTIONS ========== #
def main() -> None:
    while True:
        game_board = [f"{i}" for i in range(1, 11)]
        player_order = ["X", "O"]
        shuffle(player_order)

        for player in cycle(player_order):
            print_game_board(game_board)
            index = get_user_input(player)
            game_board[index] = player
            
            if test_for_win(game_board):
                break
                
        if not ask_for_new_match():
            quit()


# ========== EXECUTION ========== #
if __name__ == "__main__":
    main()
