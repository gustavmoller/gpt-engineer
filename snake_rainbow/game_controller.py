import pygame
from game_model import GameModel
from game_view import GameView
from constants import SCREEN_SIZE

class GameController:
    def __init__(self):
        pygame.init()
        self.model = GameModel()
        self.view = GameView(self.model, SCREEN_SIZE)
        self.clock = pygame.time.Clock()

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.model.update_direction(event.key)
            self.model.update_game_state()
            self.view.render()
            self.clock.tick(10)
        pygame.quit()