import pygame
import random
from constants import FOOD_COLOR, FOOD_SIZE, SCREEN_SIZE

class Food:
    def __init__(self):
        self.position = self.random_position()

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.position, FOOD_SIZE, FOOD_SIZE))

    def random_position(self):
        return (random.randint(0, SCREEN_SIZE[0] // FOOD_SIZE - 1) * FOOD_SIZE,
                random.randint(0, SCREEN_SIZE[1] // FOOD_SIZE - 1) * FOOD_SIZE)

    def respawn(self, snake):
        self.position = self.random_position()
        while self.position in snake.positions:
            self.position = self.random_position()