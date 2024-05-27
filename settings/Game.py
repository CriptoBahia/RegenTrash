import pygame, sys
from models.Trash import Trash
from models.Bin import Bin
from models.Types import Type
from models.builder.Director import Director
from models.builder.TrashBuilder import TrashBuilder

class Game:
    def __init__(self):
        self.trashes = []
        self.director = Director()
        self.trashBuilder = TrashBuilder()
        self.director.builder = self.trashBuilder
        self.director.build_full_featured_product()
        
        self.currentTrash = self.trashBuilder.product
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
                if self.currentTrash.parts[1].x == bin.position.x and self.currentTrash.parts[1].x.y > bin.position.y:
                    point = bin.store(self.currentTrash)
                    if point>0:
                        self.trashes.remove(self.currentTrash)
                        self.currentTrash = None
                        self.score += point
                        print(self.score)
                        break
                    