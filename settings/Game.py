import pygame, sys
from models.Trash import Trash
from models.Types import Type
from models.Bin import Bin

class Game:
    def __init__(self):
        self.trashes = []
        self.currentTrash = Trash(Type.GLASS)
        self.trashes.append(self.currentTrash)
        self.bins = []
        self.score = 0
        for i in range(0,5):
            self.bins.append(Bin(i+1, i))
        
    def update(self):
        if isinstance(self.currentTrash,Trash):
            self.currentTrash.move()
            self.checkCollision()
    
    def draw(self):
        if isinstance(self.currentTrash,Trash):
            self.currentTrash.draw()
        for bin in self.bins:
            bin.draw()
        
    def input(self, event):
        if isinstance(self.currentTrash,Trash):
            self.currentTrash.input(event)
    
    def gameOver(self):
        pygame.quit()
        sys.exit()
        
    def checkCollision(self):
        if isinstance(self.currentTrash,Trash):
            for bin in self.bins:
                if self.currentTrash.position.x == bin.position.x and self.currentTrash.position.y > bin.position.y:
                    point = bin.store(self.currentTrash)
                    if point>0:
                        self.trashes.remove(self.currentTrash)
                        self.currentTrash = None
                        self.score += point
                        print(self.score)
                        break
                    