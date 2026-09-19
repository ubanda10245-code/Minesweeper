# Project 1: Minesweeper

## Description
This project is a simple Python implementation of the classic Minesweeper game. The player works on a 10x10 grid, chooses the number of mines to place between 10 and 20, and uncovers tiles while avoiding hidden mines. The first move is made safe, and empty cells automatically reveal surrounding safe tiles.

## How to Play
- Enter a tile to reveal it, using a coordinate such as A4.
- Flag a tile using either Flag, A4 or A4, Flag.
- The game ends when a mine is uncovered, showing all mine locations.
- The player wins when every non-mine tile has been uncovered.

## Controls
- Reveal a tile: A4
- Flag or unflag a tile: Flag, A4
- Alternate flag format: A4, Flag

## Features
- 10x10 board
- adjustable mine count between 10 and 20
- first-click safety
- automatic clearing of empty spaces
- flagging and unflagging support
- loss reveal of all mines

## Requirements
- Python 3

## Project Structure
```
Minesweeper/
├── README.md
├── doc/
│   ├── 01 - System Architecture
│   └── 02 - Meeting logs
└── src/
    ├── board.py
    ├── display.py
    ├── game_logic.py
    ├── main.py
    └── player_input.py
```

## How to Run
From the project root, run:

```bash
python src/main.py
```

The program will prompt for the mine count and then begin the game.
