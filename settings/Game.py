import pygame, sys
from models.Trash import Trash
from models.builder.Director import Director
from models.builder.TrashBuilder import TrashBuilder
from models.builder.BinBuilder import BinBuilder
from .Screen import Screen
from .Config import Config

DELAY = 3000

class Game(Screen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.last_build = 0
        self.trashes = []
        self.bins = []
        self.director = Director()
        self.trashBuilder = TrashBuilder(self.surface, self.cellSize)
        self.binBuilder = BinBuilder(self.surface, self.cellSize)
        self.buildBins()
        self.currentTrash = self.buildTrash()
        self.score = 0
        
    def update(self):
        if self.checkDelay():
            self.buildTrash()
        if self.checkList():
            for trash in self.trashes:
                trash.update()
            self.checkCollision()
    
    def draw(self):
        if self.checkList():
            for trash in self.trashes:
                trash.draw()
        for bin in self.bins:
            bin.draw()
        self.drawScore()
        
    def input(self, eventType, keys):
        if self.currentTrash != None:
            self.currentTrash.input(eventType, keys)
         
    def gameOver(self):
        pygame.quit()
        sys.exit()
        
    def checkCollision(self):
        if self.currentTrash != None:
            for bin in self.bins:
                if bin.parts[3].colliderect(self.currentTrash.parts[4]):
                    self.score += bin.store(self.currentTrash)
                    self.trashes.remove(self.currentTrash)
                    self.currentTrash = None
                    return 
            if self.currentTrash.parts[1].y > self.surface.get_height():
                self.score += -100
                self.currentTrash.die()
                self.trashes.remove(self.currentTrash)
                self.currentTrash = None
                return
                  
    def drawScore(self):
        scoreFont = pygame.font.SysFont("comicsansms", 30)
        scoreSufarce = scoreFont.render(str(self.score), True, (0,0,0))
        scoreRect = scoreSufarce.get_rect()
        scoreRect.topright = ((self.surface.get_width()), (0))
        self.surface.blit(scoreSufarce, scoreRect)  
                    
    def buildTrash(self) -> Trash:
        self.director.builder = self.trashBuilder
        self.director.build_full_featured_product()
        newTrash = self.trashBuilder.product
        self.trashes.append(newTrash)
        self.last_build = pygame.time.get_ticks()
        return newTrash
        
    def buildBins(self) -> None:
        self.director.builder = self.binBuilder
        for i in range(0,4):
            self.director.build_full_featured_product()
            self.bins.append(self.binBuilder.product)
            
    def checkList(self) -> bool:
        if len(self.trashes) > 0:
            if self.currentTrash == None or len(self.currentTrash.parts) ==0:
                self.currentTrash = self.nextTrash()
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