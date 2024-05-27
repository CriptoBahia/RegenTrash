import pygame, random
from pygame.math import Vector2
from settings.Config import cellSize, screen, screenHeight, screenWidth

class Bin:
    def __init__(self, type, order):
        self.type = type
        self.position = Vector2(screenWidth*(order*2+1)/10, screenHeight*4/5)
        self.speed = 0
        self.sprite = 0
        self.surface = pygame.Surface((cellSize*1, cellSize*1))
        
    def draw(self):
        self.surface.fill((0,0,255))
        screen.blit(self.surface, (self.position.x, self.position.y))
    
    def store(self, trash):
        trash.die()
        del trash
        return 10