'''
Description: This file contains functions to display the 
current state of the grid and the cells' current state.
'''

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