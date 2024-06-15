## PONG Game in Python

This is a simple implementation of the classic PONG game using the Pygame library in Python.

### Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Running the Game](#running-the-game)
5. [Game Controls](#game-controls)
6. [Code Explanation](#code-explanation)
7. [License](#license)

### Introduction
This project recreates the classic PONG game, where two players control paddles to bounce a ball back and forth across the screen. The game is written in Python and uses the Pygame library to handle graphics and user input.

### Requirements
- Python 3.x
- Pygame library

### Setup
1. **Install Python**:
   Download and install Python from the official [Python website](https://www.python.org/).

2. **Install Pygame**:
   You can install the Pygame library using pip:
   ```bash
   pip install pygame
   ```

3. **Download the Code**:
   Clone this repository or download the code files.

### Running the Game
Navigate to the directory where you have saved the code files and run the following command:
```bash
python pong_game.py
```

### Game Controls
- **Start Game**: Press the `SPACE` key to start the game.
- **Left Paddle**:
  - Move Up: Press the `W` key.
  - Move Down: Press the `S` key.
- **Right Paddle**:
  - Move Up: Press the `UP ARROW` key.
  - Move Down: Press the `DOWN ARROW` key.

### Code Explanation

#### Constants
- `SCREEN_WIDTH` and `SCREEN_HEIGHT` define the size of the game window.
- `COLOR_BLACK` and `COLOR_WHITE` are color definitions used for the background and game elements.

#### Main Function
The `main` function initializes the Pygame modules, sets up the game window, and contains the main game loop.

#### Game Initialization
- The game window is set up with the specified width and height.
- The game title is set to "PONG".
- The clock object is created to control the frame rate.

#### Game Elements
- Two paddles (`paddle_left_rect` and `paddle_right_rect`) and one ball (`ball_rect`) are created using Pygame's `Rect` class.
- Initial movement speeds for the paddles are set to zero.
- Random initial speeds for the ball are generated.

#### Main Game Loop
- The game screen is cleared and filled with the background color.
- The event queue is processed to handle user inputs:
  - Quit event to close the game.
  - Keydown and keyup events to control paddle movements and start the game.
- The game updates the positions of the paddles and the ball based on user input and game rules.
- Collision detection ensures the ball bounces off the paddles and the top/bottom edges of the screen.
- If the ball goes off the left or right edge, the game resets and waits for the `SPACE` key to be pressed again.
- The game elements are drawn on the screen.
- The display is updated to reflect the current state of the game.

### License
This project is open-source and available under the MIT License.

