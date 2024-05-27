import pygame, sys
from models.Trash import Trash
from models.Types import Type

class Game:
    def __init__(self):
        self.trash = Trash(Type.GLASS)
        
    def update(self):
        self.trash.move()
    
    def draw(self):
        self.trash.draw()
    
    def gameOver(self):
        pygame.quit()
        sys.exit()