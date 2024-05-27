import pygame, sys
from models.Trash import Trash
from models.Types import Type
from models.Bin import Bin

class Game:
    def __init__(self):
        self.trash = Trash(Type.GLASS)
        self.bins = []
        for i in range(0,5):
            self.bins.append(Bin(i+1, i))
        
        
    def update(self):
        self.trash.move()
    
    def draw(self):
        self.trash.draw()
        for bin in self.bins:
            bin.draw()
        
    def input(self, event):
        self.trash.input(event)
    
    def gameOver(self):
        pygame.quit()
        sys.exit()