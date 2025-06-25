# 2048 Terminal Game (Python + curses)
This is a simple terminal-based version of the game **2048**, implemented in Python using the `curses` module for keyboard input.

## How to Play
- Use the **arrow keys** to move tiles up, down, left, or right.
- When two tiles with the same number collide, they **merge into one** with double the value.
- After every valid move, a new tile (2 or 4) appears at a random empty location.
- The game ends when **no more moves** are possible.
- Press **'q'** to quit the game at any time.

## Features
- Dynamic 4x4 board rendered in the terminal
- Supports all standard 2048 mechanics:
  - Tile merging
  - Score tracking
  - Game over detection
- Smooth arrow key input using `curses`
- Real-time UI updates

## Run the Game
Ensure you have Python installed (version 3.6 or above).

### 1. Clone or download the repo

### 2. Run the game
python3 game.py

Note: This script uses the curses module, which works best in Unix-based terminals (Linux/macOS). On Windows, consider using Windows Terminal or WSL (Windows Subsystem for Linux) for best results.

File Structure
2048.py – main game logic and interface
README.md – this file

Example Gameplay (Terminal View)
2048 Game | Score: 4
+----+----+----+----+
|    |    |    |  2 |
+----+----+----+----+
|    |    |    |  2 |
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
Use arrow keys to move. Press 'q' to quit.

## How it Works
Matrix Transformations: Moves are computed via row-wise operations (e.g., compressing and merging) and 90° board rotations to simulate up/down moves.

Score Calculation: The score is the sum of all tile values on the board.

Game Over Check: If no zeros or adjacent equal values exist, the game ends.

##Acknowledgments
Inspired by the original 2048 game by Gabriele Cirulli.
