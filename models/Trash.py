import pygame, random
from pygame.math import Vector2
from settings.Config import cellSize, screen

class Trash:
    def __init__(self, type):
        self.type = type
        self.position = Vector2(400, 0)
        self.speed = 20
        self.sprite = 0
        self.surface = pygame.Surface((cellSize*1, cellSize*1))
        
    def draw(self):
        self.surface.fill((255,255,255))
        screen.blit(self.surface, (self.position.x, self.position.y))
        
    def move(self):
        self.position.y+=self.speed
        
    def input(self,event):
        match event:
            case pygame.K_LEFT:
                self.position.x-=self.speed*2
            case pygame.K_RIGHT:
                self.position.x+=self.speed*2