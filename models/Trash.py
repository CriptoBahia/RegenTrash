import pygame
from settings.Config import SCREEN

class Trash:
    def __init__(self):
        self.parts = []
        
    def add(self, part: any) -> None:
        self.parts.append(part)
        
    def list_parts(self) -> None:
        for i in self.parts:
            print(i)
        
    def draw(self):
        SCREEN.blit(self.parts[3], (self.parts[1].x, self.parts[1].y))
        
    def input(self, eventType, keys):
        if eventType == pygame.KEYUP:
            self.parts[5].x = 0
            self.parts[5].y = self.parts[2]
        elif eventType == pygame.KEYDOWN:
            if keys[pygame.K_LEFT]:
                self.parts[5].x = -self.parts[2]*2
            if keys[pygame.K_RIGHT]:
                self.parts[5].x = self.parts[2]*2
            if keys[pygame.K_DOWN]:
                self.parts[5].y = self.parts[2]*2
            if keys[pygame.K_UP]:
                self.parts[5].y = self.parts[2]/2
    
    def update(self):
        self.parts[1].x += self.parts[5].x
        self.parts[1].y += self.parts[5].y
        self.parts[4] = self.parts[3].get_rect(center=(self.parts[1].x,self.parts[1].y))
        
    def die(self):
        self.parts[3] = None  
        del self