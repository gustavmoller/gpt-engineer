import pygame

# Screen dimensions
SCREEN_SIZE = (600, 400)

# Colors
BACKGROUND_COLOR = (0, 0, 0)
# SNAKE_COLOR is removed as we will use RAINBOW_COLORS for the snake
FOOD_COLOR = (255, 0, 0)
RAINBOW_COLORS = [
    (148, 0, 211),  # Violet
    (75, 0, 130),   # Indigo
    (0, 0, 255),    # Blue
    (0, 255, 0),    # Green
    (255, 255, 0),  # Yellow
    (255, 127, 0),  # Orange
    (255, 0, 0),    # Red
]

# Sizes
SNAKE_SIZE = 10
FOOD_SIZE = 10

# Directions
DIRECTIONS = {
    pygame.K_UP: (0, -SNAKE_SIZE),
    pygame.K_DOWN: (0, SNAKE_SIZE),
    pygame.K_LEFT: (-SNAKE_SIZE, 0),
    pygame.K_RIGHT: (SNAKE_SIZE, 0),
}