'''
Description: This file contains functions to handle player input and display mine locations after a loss.
'''

def get_player_input(grid, uncover_action, flag_action):
    """
    Get input from the player and execute the corresponding action.
    Args:
        grid (2D list): 2D representation of the grid
        uncover_action (function): Function to uncover a cell
        flag_action (function): Function to flag a cell
    """
    """Command format:
        A4
        A4, Flag
        Flag, A4 """
    
    print("\nEnter a command in the format 'A4' to uncover a cell or 'A4, Flag' to flag a cell.")
    command = input("Enter command: ").strip()

    # separate the cell and action using the comma
    parts = [part.strip() for part in command.split(",")]

    if len(parts) == 1:
        cell_name = parts[0].upper() # convert to uppercase

        try:
            col = ord(cell_name[0]) - ord('A') # convert letter to column index
            row = int(cell_name[1:]) - 1 # convert number to row index

        except (IndexError, ValueError):
            print("Invalid command")
            return

        if 0 <= row < len(grid) and 0 <= col < len(grid):
            uncover_action(grid, row, col)
        else:
            print("Invalid cell.")

    # handle flagging command
    elif len(parts) == 2:
        if parts[0].upper() == "FLAG":
            cell_name = parts[1].upper()
        elif parts[1].upper() == "FLAG":
            cell_name = parts[0].upper()
        else:
            print("Invalid command.")
            return

        try:
            col = ord(cell_name[0]) - ord('A')
            row = int(cell_name[1:]) - 1
        except (IndexError, ValueError):
            print("Invalid command")
            return

        if 0 <= row < len(grid) and 0 <= col < len(grid):
            flag_action(grid, row, col)
        else:
            print("Invalid cell.")
    else:
        print("Invalid command.")

def show_mines(grid): # show location of mines after loss
    """Show the locations of all mines on the grid.
    Args:
        grid (2D list): 2D representation of the grid
    """
    print("\nMine locations:")
    size = len(grid)

    col_labels = [chr(ord('A') + i) for i in range(size)]
    print('   ' + ' '.join(col_labels))

    for row_index, row in enumerate(grid):
        print(f'{row_index + 1:2} ', end = '')

        for cell in row:
            if cell.is_mine:
                print('*', end = ' ')
            else:
                print('.', end = ' ')
        print()
