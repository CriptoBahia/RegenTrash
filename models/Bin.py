import pygame, random
from pygame.math import Vector2
from settings.Config import cellSize, screen, screenHeight, screenWidth

class Bin:
    
    def __init__(self):
        self.parts = []   
        
    def add(self, part: any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        for i in self.parts:
            print(i)
        
    def draw(self):
        self.parts[3].fill((0,0,255))
        screen.blit(self.parts[3], (self.parts[1].x, self.parts[1].y))
    
    def store(self, trash):
        trash.die()
        del trash
        return 10