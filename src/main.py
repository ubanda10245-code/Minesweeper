'''
Description: This is the main file for the Minesweeper game. 
It contains the main game loop, as well as the functions for creating the grid, placing mines, 
counting adjacent mines, uncovering cells, and checking the game status.
It imports the get_player_input and show_mines functions from the player_input.py file.
'''

import random

# ========================= BOARD MANAGER ==========================

class Cell:
    """Class for grid cell's states and adjacent mine counter
    """
    def __init__(self):
        self.is_mine = False
        self.is_uncovered = False
        self.is_flagged = False
        self.adjacent_mines = 0 # ranges from 0 to 8


def create_grid(size):
    """Create the 2D list representation of the grid
    Args:
        size (int): The row and column length of the minesweeper grid.
    Returns:
        A 2D list containing only Cell objects.
    """
    return [[Cell() for _ in range(size)] for _ in range(size)]

# ========================= GAME LOGIC =========================

# Mine configuration functions
def get_mine_count(min_mines=10, max_mines=20):
    """Prompt the user for the desired mine count (10-20) with input validation.
    Args:
        min_mines (int): The minimum amount of mines allowed
        max_mines (int): The maximum amount of mines allowed
    Returns:
        int: The number of mines the user has chosen.
    """
    while True:
        try:
            mines = int(input(f"Enter the desired number of mines ({min_mines}-{max_mines}): "))
            if min_mines <= mines <= max_mines:
                return mines
            print(f"Invalid choice. Please enter a number between {min_mines} and {max_mines}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def place_mines(grid, mine_count):
    """Randomly place the mines on the grid.
    Args:
        grid (2D list): 2D representation of the grid
        mine_count (int): The desired amount of mines to be placed
    """
    size = len(grid)
    all_positions = [(r, c) for r in range(size) for c in range(size)]
    
    # Pick unique random coordinates
    mine_positions = random.sample(all_positions, mine_count)    

    for r, c in mine_positions:
            grid[r][c].is_mine = True


def make_first_move_safe(grid, row, col):
    """Move a mine away from the first cell selected by the player.
    Args:
        grid (2D list): 2D representation of the grid
        row (int): Row index of the selected cell
        col (int): Column index of the selected cell
    Return:
        (none) This exits the function if the selected mine is not a mine.
    """
    selected_cell = grid[row][col]

    if not selected_cell.is_mine:
        return

    # Store locations on the grid that do not contain a mine
    safe_positions = [
        (current_row, current_col)
        for current_row in range(len(grid))
        for current_col in range(len(grid))
        if not grid[current_row][current_col].is_mine
        and (current_row, current_col) != (row, col)
    ]

    # Move the mine to any safe_positions and make the selected cell safe
    new_row, new_col = random.choice(safe_positions)
    selected_cell.is_mine = False
    grid[new_row][new_col].is_mine = True

    # Recalculate counts because the mine positions changed.
    for current_row in grid:
        for cell in current_row:
            cell.adjacent_mines = 0
    count_adjacent_mines(grid)
        
def count_adjacent_mines(grid):
    """Update the adjacent mine count for each cell
    Args:
        grid (2D list): 2D representation of the grid
    """
    size = len(grid)

    for row in range(size):
        for col in range(size):
            if grid[row][col].is_mine:

                # Check the 8 cells around the mine
                for row_change in [-1, 0, 1]:
                    for col_change in [-1, 0, 1]:
                        new_row = row + row_change
                        new_col = col + col_change

                        # Make sure the cell is inside the grid
                        if 0 <= new_row < size and 0 <= new_col < size:

                            # Do not count the mine itself
                            if new_row != row or new_col != col:
                                grid[new_row][new_col].adjacent_mines += 1

def count_flags(grid):
    """Sum the amount of flags on the grid
    Args:
        grid (2D list): 2D representation of the grid
    Returns:
        int : The total number of flags placed on the grid
    """
    return sum(cell.is_flagged for row in grid for cell in row)
 
def remaining_mines(grid, total_mines):
    """Calculate the number of remaining mines to flag (assuming that all flags 
    have been placed correctly)
    Args:
        grid (2D): 2D representation of the grid
        total_mines (int): The total number of mines
    Returns:
        int: The remaining amount of mines left
    """
    return total_mines - count_flags(grid)

def check_game_status(grid):
    """Determine whether the player has won, lost, or playing
    Args:
        grid (2D): 2D representation of the grid
    Returns:
        str: Return game status of the player
    """
    # Player has uncovered a mine
    for row in grid:
        for cell in row:
            if cell.is_uncovered and cell.is_mine:
                return "Game Over: Loss"

    # Player has yet to uncover all cells without mines
    for row in grid:
        for cell in row:
            if not cell.is_mine and not cell.is_uncovered:
                return "Playing"
 
    return "Victory"

def uncover_cell(grid, row, col):
    """Uncover a selected cell.
    Args:
        grid (2D list): 2D representation of the grid
        row (int): Row index of the selected cell
        col (int): Column index of the selected cell
    Returns:
        None
    """
    cell = grid[row][col]

    #don't uncover a flagged cell.
    if cell.is_flagged:
        print("Cannot uncover a flagged cell.")
        return

    cells_to_visit = [(row, col)]
    visited = set()

    while cells_to_visit:
        current_row, current_col = cells_to_visit.pop()

        if (current_row, current_col) in visited: #Checks that the current tile has not already been evaluated 
            continue

        visited.add((current_row, current_col))
        current_cell = grid[current_row][current_col]

        if current_cell.is_flagged:
            continue
        current_cell.is_uncovered = True

        if current_cell.is_mine:
            continue

        if current_cell.adjacent_mines != 0: #Don't need to continue expansion on cells with neighboring mines
            continue

        for row_change in [-1, 0, 1]:
            for col_change in [-1, 0, 1]:
                if row_change == 0 and col_change == 0: #Skips comparison with itself 
                    continue

                new_row = current_row + row_change
                new_col = current_col + col_change

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid): #Validates tile
                    neighbor = grid[new_row][new_col]
                    if not neighbor.is_flagged and not neighbor.is_mine: #Adds non mines to potential auto-uncover candidates
                        cells_to_visit.append((new_row, new_col))


def create_first_move_handler():
    """Return an uncover action that protects only the first uncover.
    Returns:
        function: A function that uncovers a cell and makes the first move safe.
    """
    first_uncover = True

    def uncover_with_first_move_safe(grid, row, col):
        """ Uncover a cell and make the first move safe if it's the first uncover.
        Args:
            grid (2D list): 2D representation of the grid
            row (int): Row index of the selected cell
            col (int): Column index of the selected cell
        """
        nonlocal first_uncover

        if first_uncover:
            make_first_move_safe(grid, row, col)
            first_uncover = False

        uncover_cell(grid, row, col)

    return uncover_with_first_move_safe


def flag_cell(grid, row, col):
    """Toggle the flag on a selected cell.
    Args:
        grid (2D list): 2D representation of the grid
        row (int): Row index of the selected cell
        col (int): Column index of the selected cell
    Returns:
        None
    """
    cell = grid[row][col]

    # Do not allow an uncovered cell to be flagged.
    if cell.is_uncovered:
        print("Cannot flag a cell that has already been uncovered.")
        return

    # Toggle the flag.
    cell.is_flagged = not cell.is_flagged

# ========================= USER INTERFACE =========================

def print_grid(grid):
    """Print the current state of the grid and the cells' current state.
    Args:
        grid (2D): 2D representation of the grid
    """
    size = len(grid)

    # print column letters
    col_labels = [chr(ord('A') + i) for i in range(size)]
    print('   ' + ' '.join(col_labels))

    for row_index, row in enumerate(grid):
        # print row number
        print(f'{row_index + 1:2} ', end='')

        for cell in row:
            # Print the cell's state 
            if cell.is_uncovered:
                if cell.is_mine:
                    print('*', end=' ')
                else:
                    print(cell.adjacent_mines, end=' ')
            elif cell.is_flagged:
                print('F', end=' ')
            else:
                print('.', end=' ')
        print()

# ================= INPUT HANDLER =================

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