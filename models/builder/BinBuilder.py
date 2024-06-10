from .Builder import Builder
from ..Bin import Bin 
from ..Type import Type
from pygame import Vector2
import pygame
from settings.Resolution import Resolution

class BinBuilder(Builder):

    def __init__(self, surface: pygame.surface, cellSize: int) -> None:
        self._surface = surface
        self.cellSize = cellSize
        self.order = [0,0]
        self.SPEED = 0
        self.COLORS = [(0, 0, 255), (0, 255, 0), (255, 128, 0), (255, 255, 0), (128, 128, 128)]
        self.reset()

    def reset(self) -> None:
        self._product = Bin(self._surface)

    @property
    def product(self) -> Bin:
        product = self._product
        self.reset()
        return product

    def produce_type(self) -> None:
        self._product.add(Type(self.order[0]+1))
        
    def produce_position(self) -> None:
        if self.order[1]>=2 and self.order[1]<4:
            self.order[1] = 4
        self.binX = self.order[1]*self._surface.get_width()/6+self._surface.get_width()/20
        print(self.binX)
        self.binY = self._surface.get_height()*4/5
        self._product.add(Vector2(self.binX, self.binY))
        self.order[0]+=1
        self.order[1]+=1
    
    def produce_speed(self) -> None:
        pass
    
    def produce_sprite(self) -> None:
        path = "models/sprites/bins/"+self._product.parts[0].name+"_reciclying_bin.png"
        sprite = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (self.cellSize*2, self.cellSize*2))
        self._product.add(sprite)
        
    def produce_rect(self) -> None:
        self._product.add(self._product.parts[2].get_rect(center=(self.binX, self.binY)))
    
    def produce_direction(self) -> None:
        pass