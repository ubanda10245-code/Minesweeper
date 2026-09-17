import random

'''
Initialize a basic minesweeper template
'''

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
    """
    size = len(grid)
    all_positions = [(r, c) for r in range(size) for c in range(size)]
    
    # Pick unique random coordinates
    mine_positions = random.sample(all_positions, mine_count)
    
    for r, c in mine_positions:
        grid[r][c].is_mine = True
        
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

    # Uncover the selected cell.
    cell.is_uncovered = True


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

# Not implemented yet

if __name__ == "__main__":
    grid = create_grid(10)

    # Prompt user for mine count and place them
    total_mines = get_mine_count(10, 20)
    place_mines(grid, total_mines)
    count_adjacent_mines(grid)

    # Main game loop
    while check_game_status(grid) == "Playing":
        print_grid(grid)
        print(f"Mines remaining: {remaining_mines(grid, total_mines)}")
        print(f"Status: {check_game_status(grid)}")

        # Temporary input for testing the uncover function.
        # This will be replaced by the input handler in Task 8.
        try:
            row = int(input("Enter row (1-10): ")) - 1
            col = int(input("Enter column (1-10): ")) - 1

            # Make sure the selected cell is inside the grid.
            if 0 <= row < len(grid) and 0 <= col < len(grid):
                uncover_cell(grid, row, col)
            else:
                print("Invalid cell. Please enter a row and column from 1 to 10.")

        except ValueError:
            print("Invalid input. Please enter numbers for the row and column.")

    # Display the final game state.
    print_grid(grid)
    print(f"Mines remaining: {remaining_mines(grid, total_mines)}")
    print(f"Status: {check_game_status(grid)}")

