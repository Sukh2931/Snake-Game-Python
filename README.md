# 🐍 Snake Game Using Python

## Project Overview
Snake Game is a desktop-based game developed using Python and Pygame. The player controls a snake using arrow keys and collects food to increase its length and score.

The game becomes faster as the snake grows.

## Features
- Simple user interface
- Smooth snake movement
- Arrow key controls
- Random food generation
- Score tracking
- Best score saving
- Collision detection
- Pause and resume
- Restart option
- Increasing game speed

## Technologies Used
- Python
- Pygame
- Random module
- File Handling

## Installation

Install Pygame:

```bash
python3 -m pip install pygame
```

## How to Run

```bash
python3 snake_game.py
```

## Game Controls

| Key | Function |
|---|---|
| Arrow Keys | Move snake |
| Space | Start game |
| P | Pause or resume |
| R | Restart |
| Esc | Exit |

## Special Feature

The game speed increases as the score increases.

```python
speed = min(5 + (score // 20), 20)
```

## Learning Outcomes
- Python functions and loops
- Conditional statements
- Lists and random numbers
- Pygame event handling
- Collision detection
- File handling

## Author
Sukhdeep

## Course
BCA – Python Programming
