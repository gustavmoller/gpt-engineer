import pygame
from constants import RAINBOW_COLORS, SNAKE_SIZE, DIRECTIONS

class Snake:
    def __init__(self):
        self.positions = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT

    def move(self, direction):
        current = self.positions[0]
        x, y = current
        dx, dy = DIRECTIONS[direction]
        new_head = (x + dx, y + dy)
        self.positions = [new_head] + self.positions[:-1]

    def draw(self, screen):
        for index, position in enumerate(self.positions):
            color_index = index % len(RAINBOW_COLORS)
            pygame.draw.rect(screen, RAINBOW_COLORS[color_index], (*position, SNAKE_SIZE, SNAKE_SIZE))

    def head_position(self):
        return self.positions[0]

    def grow(self):
        self.positions.append(self.positions[-1])

    def get_opposite_direction(self):
        if self.direction == pygame.K_UP:
            return pygame.K_DOWN
        elif self.direction == pygame.K_DOWN:
            return pygame.K_UP
        elif self.direction == pygame.K_LEFT:
            return pygame.K_RIGHT
        elif self.direction == pygame.K_RIGHT:
            return pygame.K_LEFT

    def has_collided(self):
        head = self.head_position()
        return head in self.positions[1:]

    def is_in_bounds(self, screen_size):
        x, y = self.head_position()
        return 0 <= x < screen_size[0] and 0 <= y < screen_size[1]