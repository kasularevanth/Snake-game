# Snake Game

This project is a classic **Snake Game** built using Python and Pygame. The game involves controlling a snake to collect apples while avoiding collisions with walls and its own body. With every apple collected, the snake grows longer, and the score increases.

## Features

- **User Controls**: Use arrow keys to control the snake's movement.
- **Dynamic Gameplay**: The snake grows with every apple collected.
- **Pause/Resume**: Press `P` to pause or resume the game.
- **Start Screen**: A welcoming start screen prompts the user to begin.
- **Game Over Screen**: Displays the score with options to restart or exit.

## Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right).
- **Enter**: Start or restart the game.
- **Escape**: Quit the game.
- **P**: Pause/Resume the game.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Install Python: [Download Python](https://www.python.org/)
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Download or clone the project files.

## How to Play

1. Run the game:
   ```bash
   python snake_game.py
   ```
2. Press **Enter** to start.
3. Use arrow keys to navigate the snake.
4. Avoid hitting the walls or the snake's own body.
5. Collect apples to increase your score.
6. Press **P** to pause or resume as needed.
7. When the game ends, press **Enter** to restart or **Escape** to exit.

## Game Design

- **Snake**: Composed of blocks represented by an image (`img/block.jpg`).
- **Apple**: Randomly placed on the screen (`img/apple.jpg`).
- **Background**: A purple-themed interface (`RGB: 137, 119, 181`).
- **Score**: Displayed at the top-left corner of the screen.

## File Structure

- `snake_game.py`: Main game logic.
- `img/block.jpg`: Snake block image.
- `img/apple.jpg`: Apple image.

## Future Enhancements

- Add levels with increasing difficulty.
- Introduce obstacles.
- Add sound effects for gameplay events.

Enjoy the game!

