'''
Description: This file contains the Cell class and the create_grid function for the Minesweeper game.
The Cell class represents each cell in the grid, with attributes for mine status, 
uncover status, flag status, and adjacent mine count. 
The create_grid function generates a 2D list of Cell objects.
'''
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