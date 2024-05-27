import pygame, random
from pygame.math import Vector2
from settings.Config import cellSize, screen

class Trash:
    def __init__(self):
        self.parts = []
        
    def add(self, part: any) -> None:
        self.parts.append(part)
        
    def list_parts(self) -> None:
        for i in self.parts:
            print(i)
        
    def draw(self):
        if isinstance(self, Trash):
            self.parts[3].fill((255,255,255))
            screen.blit(self.parts[3], (self.parts[1].x, self.parts[1].y))
        
    def move(self):
        self.parts[1].y+=self.parts[2]
        
    def input(self,event):
        match event:
            case pygame.K_LEFT:
                self.parts[1].x-=self.parts[2]*2
            case pygame.K_RIGHT:
                self.parts[1].x+=self.parts[2]*2
    
    def die(self):
        self.parts[3] = None  
                
    def __del__(self):
        print("Deleted.")
                
                
    