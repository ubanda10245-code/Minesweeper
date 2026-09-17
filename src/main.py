import random

'''
Initialize a basic minesweeper template
'''

# Cell class of grid cell states and adjacent mine counter
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_uncovered = False
        self.is_flagged = False
        self.adjacent_mines = 0 # ranges from 0 to 8

# Return a array of cells 
def create_grid(size):
    return [[Cell() for _ in range(size)] for _ in range(size)]

# Mine configuration functions
def get_mine_count(min_mines=10, max_mines=20):
    """Prompt the user for the desired mine count (10-20) with input validation."""
    while True:
        try:
            mines = int(input(f"Enter the desired number of mines ({min_mines}-{max_mines}): "))
            if min_mines <= mines <= max_mines:
                return mines
            print(f"Invalid choice. Please enter a number between {min_mines} and {max_mines}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def place_mines(grid, mine_count):
    """Randomly place the mines on the grid."""
    size = len(grid)
    all_positions = [(r, c) for r in range(size) for c in range(size)]
    
    # Pick unique random coordinates
    mine_positions = random.sample(all_positions, mine_count)
    
    for r, c in mine_positions:
        grid[r][c].is_mine = True
        
# Update the adjacent mine count for each cell
def count_adjacent_mines(grid):
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

# Return how many cells are flagged
def count_flags(grid):
    return sum(cell.is_flagged for row in grid for cell in row)
 
# Return the remaining amount of mines left
def remaining_mines(grid, total_mines):
    return total_mines - count_flags(grid)

# Print the current state of the grid and the cells' current state.
def print_grid(grid):
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

# Return game status of the player
def check_game_status(grid):
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

if __name__ == "__main__":
    grid = create_grid(10)

    # Prompt user for mine count and place them
    total_mines = get_mine_count(10, 20)
    place_mines(grid, total_mines)
    count_adjacent_mines(grid)

    # For testing: uncover all cells so you can see where the mines are
    for row in grid:
        for cell in row:
            cell.is_uncovered = True

    print(f"Mines remaining: {remaining_mines(grid, total_mines)}")
    print(f"Status: {check_game_status(grid)}")
    print_grid(grid)
