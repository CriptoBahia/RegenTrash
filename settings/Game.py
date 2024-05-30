import pygame, sys
from models.Trash import Trash
from models.Bin import Bin
from models.Types import Type
from models.builder.Director import Director
from models.builder.TrashBuilder import TrashBuilder
from models.builder.BinBuilder import BinBuilder


DELAY = 2000

class Game:
    def __init__(self):
        self.last_build = None
        self.trashes = []
        self.bins = []
        self.director = Director()
        self.trashBuilder = TrashBuilder()
        self.binBuilder = BinBuilder()
        self.buildBins()
        self.currentTrash = self.buildTrash()
        self.score = 0
        
    def update(self):
        if self.checkDelay():
            self.buildTrash()
        if self.checkList():
            for trash in self.trashes:
                trash.move()
            self.checkCollision()
    
    def draw(self):
        if self.checkList():
            for trash in self.trashes:
                trash.draw()
        for bin in self.bins:
            bin.draw()
        
    def input(self, event):
        if isinstance(self.currentTrash,Trash):
            self.currentTrash.input(event)
    
    def gameOver(self):
        pygame.quit()
        sys.exit()
        
    def checkCollision(self):
            for bin in self.bins:
                if self.currentTrash.parts[1].x == bin.parts[1].x and self.currentTrash.parts[1].y > bin.parts[1].y:
                    point = bin.store(self.currentTrash)
                    if point>0:
                        self.trashes.remove(self.currentTrash)
                        self.currentTrash = self.nextTrash()
                        self.score += point
                        print(self.score)
                        break
                    
                    
    def buildTrash(self) -> Trash:
        self.director.builder = self.trashBuilder
        self.director.build_full_featured_product()
        newTrash = self.trashBuilder.product
        self.trashes.append(newTrash)
        self.last_build = pygame.time.get_ticks()
        return newTrash
        
    def buildBins(self) -> None:
        self.director.builder = self.binBuilder
        for i in range(0,5):
            self.director.build_full_featured_product()
            self.bins.append(self.binBuilder.product)
            
    def checkList(self) -> bool:
        if len(self.trashes) > 0:
            return True
        return False
                    
    def checkDelay(self) -> bool:
        time_since_build = pygame.time.get_ticks() - self.last_build
        if time_since_build > DELAY:
            return True
        return False
    
    def nextTrash(self) -> Trash:
        iterator = iter(self.trashes)
        return next(iterator)