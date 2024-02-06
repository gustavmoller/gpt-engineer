import pygame
from snake import Snake
from food import Food
from constants import DIRECTIONS, SCREEN_SIZE

class GameModel:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.direction = pygame.K_RIGHT

    def update_direction(self, key):
        if key in DIRECTIONS and DIRECTIONS[key] != self.snake.get_opposite_direction():
            self.direction = key

    def update_game_state(self):
        self.snake.move(self.direction)
        if self.snake.head_position() == self.food.position:
            self.snake.grow()
            self.food.respawn(self.snake)

        if self.snake.has_collided() or not self.snake.is_in_bounds(SCREEN_SIZE):
            self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.direction = pygame.K_RIGHT