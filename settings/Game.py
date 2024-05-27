import pygame, sys
from models.Trash import Trash
from models.Bin import Bin
from models.Types import Type
from models.builder.Director import Director
from models.builder.TrashBuilder import TrashBuilder
from models.builder.BinBuilder import BinBuilder

class Game:
    def __init__(self):
        self.trashes = []
        self.director = Director()
        self.trashBuilder = TrashBuilder()
        self.binBuilder = BinBuilder()
        self.director.builder = self.binBuilder
        self.bins = []
        for i in range(0,5):
            self.director.build_full_featured_product()
            self.bins.append(self.binBuilder.product)
        self.director.builder = self.trashBuilder
        self.director.build_full_featured_product()
        self.currentTrash = self.trashBuilder.product
        self.trashes.append(self.currentTrash)
        
        self.score = 0
        
        
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
                if self.currentTrash.parts[1].x == bin.parts[1].x and self.currentTrash.parts[1].y > bin.parts[1].y:
                    point = bin.store(self.currentTrash)
                    if point>0:
                        self.trashes.remove(self.currentTrash)
                        self.currentTrash = None
                        self.score += point
                        print(self.score)
                        break
                    