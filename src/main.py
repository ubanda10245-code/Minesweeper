'''
Description: This is the main file for the Minesweeper game. 
It contains the main game loop, as well as the functions for creating the grid, placing mines, 
counting adjacent mines, uncovering cells, and checking the game status.
It imports the get_player_input and show_mines functions from the player_input.py file.
'''

import random
from board import create_grid
from display import print_grid
from game_logic import (
    get_mine_count,
    place_mines,
    count_adjacent_mines,
    check_game_status,
    uncover_cell,
    flag_cell,
    remaining_mines,
    create_first_move_handler
)
from player_input import get_player_input, show_mines

# ================= MAIN GAME LOOP =================

if __name__ == "__main__":
    grid = create_grid(10)
    uncover_action = create_first_move_handler()

    # Prompt user for mine count and place them
    total_mines = get_mine_count(10, 20)
    
    place_mines(grid, total_mines)
    count_adjacent_mines(grid)

    # Main game loop
    while check_game_status(grid) == "Playing":
        print_grid(grid)
        print(f"Mines remaining: {remaining_mines(grid, total_mines)}")
        print(f"Status: {check_game_status(grid)}")

        get_player_input(grid, uncover_action, flag_cell)

    final_status = check_game_status(grid)

    if final_status == "Victory":
        print("Congratulations! You've won the game!")

    # Display the final game state.
    print_grid(grid)
    print(f"Mines remaining: {remaining_mines(grid, total_mines)}")
    print(f"Status: {final_status}")

    if final_status == "Game Over: Loss":
        show_mines(grid)