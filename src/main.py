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

    total_mines = 10 # Temp mines value

    # For testing random mines locations and adjacent mines counter,
    #  assign each cell to be uncovered. This so you can see these printed
    #  on the grid.

    print(f"Mines remaining: {remaining_mines(grid, total_mines)}")
    print(f"Status: {check_game_status(grid)}")
    print_grid(grid)