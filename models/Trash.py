import pygame, random
from pygame.math import Vector2
from settings.Config import cellSize, screen

class Trash:
    def __init__(self):
        self.surface = pygame.Surface((cellSize*1, cellSize*2))
       
        
    def draw(self):
        self.surface.fill((255,255,255))
        screen.blit(self.surface, (400, 400))