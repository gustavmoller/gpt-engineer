import pygame

# Screen dimensions
SCREEN_SIZE = (600, 400)

# Colors
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

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