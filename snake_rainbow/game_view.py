import pygame
from constants import BACKGROUND_COLOR

class GameView:
    def __init__(self, model, screen_size):
        self.model = model
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('Snake Game')

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.model.snake.draw(self.screen)
        self.model.food.draw(self.screen)
        pygame.display.flip()