from .Builder import Builder
from ..Bin import Bin 
from ..Types import Type
from pygame import Vector2
import pygame
from settings.Config import CELLSIZE, SCREENHEIGHT, SCREENWIDTH

SPEED = 0
COLORS = [(0, 0, 255), (0, 255, 0), (255, 128, 0), (255, 255, 0), (128, 128, 128)]

class BinBuilder(Builder):

    def __init__(self) -> None:
        self.order = 0
        
        self.reset()

    def reset(self) -> None:
        self._product = Bin()

    @property
    def product(self) -> Bin:
        product = self._product
        self.reset()
        return product

    def produce_type(self) -> None:
        self._product.add(Type(self.order+1))
        
    def produce_position(self) -> None:
        self.binX = SCREENWIDTH*2/5+(self.order*80 - 80)
        self.binY = SCREENHEIGHT*4/5
        self._product.add(Vector2(self.binX, self.binY))
        self.order+=1
    
    def produce_speed(self) -> None:
        self._product.add(SPEED)
    
    def produce_sprite(self, sprite) -> None:
        pass
        
    def produce_surface(self) -> None:
        self._product.add(pygame.Surface((CELLSIZE, CELLSIZE)))
        self._product.parts[3].fill(COLORS[self.order-1])
    
    def produce_rect(self) -> None:
        self._product.add(self._product.parts[3].get_rect(center=(self.binX, self.binY)))
    
    def produce_direction(self) -> None:
        pass