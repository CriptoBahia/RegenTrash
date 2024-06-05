import pygame, sys
from models.Trash import Trash
from models.builder.Director import Director
from models.builder.TrashBuilder import TrashBuilder
from models.builder.BinBuilder import BinBuilder
from settings.Config import SCREEN, SCREENHEIGHT, SCREENWIDTH

DELAY = 3000

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
                if self.currentTrash.parts[1].x == bin.parts[1].x and self.currentTrash.parts[1].y > bin.parts[1].y:
                    self.score += bin.store(self.currentTrash)
                    self.trashes.remove(self.currentTrash)
                    self.currentTrash = None
                    break
                  
    def drawScore(self):
        scoreFont = pygame.font.SysFont("comicsansms", 30)
        scoreSufarce = scoreFont.render(str(self.score), True, (0,0,0))
        scoreRect = scoreSufarce.get_rect()
        scoreRect.topright = ((SCREENWIDTH), (0))
        SCREEN.blit(scoreSufarce, scoreRect)  
                    
    def buildTrash(self) -> Trash:
        try:
            self.director.builder = self.trashBuilder
            self.director.build_full_featured_product()
        except:
            print("trash build failed.")
        else:
            newTrash = self.trashBuilder.product
            self.trashes.append(newTrash)
            self.last_build = pygame.time.get_ticks()
            return newTrash
        
    def buildBins(self) -> None:
        try:
            self.director.builder = self.binBuilder
            for i in range(0,5):
                self.director.build_full_featured_product()
                self.bins.append(self.binBuilder.product)
        except:
            print("bin build failed.")
            
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