import pygame
import sys
from models.Trash import Trash

class Game:
    def __init__(self):
        self.trash = Trash()
        
    def update(self):
        pass
    
    def draw(self):
        self.trash.draw()
    
    def gameOver(self):
        pygame.quit()
        sys.exit()