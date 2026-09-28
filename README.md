# 🎮 Bälle – Pygame Game

A simple 2D game built with **Python** and **Pygame**. The player controls a character and tries to catch falling balls to increase their score.

## 📌 Description

In this game, balls randomly appear at the top of the screen and fall downward. The player controls the character using the **Left** and **Right** arrow keys.

Each caught ball gives the player **1 point**.

The game continues until the player closes the game window.

## 🕹️ Controls

| Key          | Action        |
| ------------ | ------------- |
| `←`          | Move left     |
| `→`          | Move right    |
| Close window | Exit the game |

## ✨ Features

* Player movement using the keyboard
* Randomly spawning falling balls
* Collision detection
* Score system
* Smooth movement using delta time
* 60 FPS game loop
* Custom images for the player, balls, and background

## 📁 Project Structure

```text
project/
│
├── assets/
│   ├── avatar.png
│   └── ball.png
│
├── background.jpg
├── main.py
└── README.md
```

> Replace `main.py` with the actual name of your Python file if it is different.

## 🛠️ Requirements

You need the following to run the game:

* Python 3.9+
* Pygame

Install Pygame with:

```bash
pip install pygame
```

Or:

```bash
python -m pip install pygame
```

## 🚀 Installation & Running

1. Clone the repository:

```bash
git clone <REPOSITORY_URL>
```

2. Navigate to the project directory:

```bash
cd project
```

3. Install the required dependency:

```bash
pip install pygame
```

4. Run the game:

```bash
python main.py
```

## ⚙️ Game Settings

The main game settings can be changed at the beginning of the program:

```python
WIDTH = 800
HEIGHT = 600
FPS = 60
```

### Window Size

```python
WIDTH = 800
HEIGHT = 600
```

These values define the width and height of the game window.

### Frame Rate

```python
FPS = 60
```

This defines the maximum number of frames processed per second.

### Player Speed

The player's movement speed is defined in the `Player` class:

```python
self.rect.x += 300 * dt
```

and:

```python
self.rect.x -= 300 * dt
```

The value `300` controls the player's movement speed.

### Ball Speed

The falling speed of the balls is defined in the `Star` class:

```python
self.rect.y += 150 * dt
```

The value `150` controls how quickly the balls fall.

### Ball Spawn Rate

A new ball is created approximately every second:

```python
if timer > 1:
    timer = 0
    stars.add(Star())
```

You can decrease the value `1` to make balls spawn more frequently.

## 🧩 How It Works

The game loop consists of several main stages.

### 1. Event Handling

The game checks for Pygame events, such as closing the window:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

### 2. Updating Objects

The player's and balls' positions are updated every frame.

The game uses delta time:

```python
dt = clock.tick(FPS) / 1000
```

This makes movement consistent regardless of the frame rate.

### 3. Spawning Balls

A new `Star` object is created every second at a random horizontal position at the top of the screen.

### 4. Collision Detection

When the player catches a ball:

```python
hits = pygame.sprite.spritecollide(player, stars, True)
```

The ball is removed and the score is increased:

```python
score += len(hits)
```

### 5. Rendering

Every frame, the game draws:

* the background;
* falling balls;
* the player.

The current score is displayed in the game window title:

```python
pygame.display.set_caption(f"Bälle: {score}")
```

## 🖼️ Assets

The following files are required for the game to work correctly:

```text
assets/avatar.png
assets/ball.png
background.jpg
```

Make sure these files are located in the correct directories.

## 🔧 Possible Improvements

The game could be extended with:

* Screen boundaries for the player
* Sound effects
* Background music
* Increasing ball speed over time
* A main menu
* A Game Over screen
* A high-score system
* Different types of falling objects
* Multiple difficulty levels
* An on-screen score display
* Player animations
* A lives system

## 📄 License

This project was created for educational purposes.

You can add a license such as the **MIT License** if you plan to publish the project on GitHub.
