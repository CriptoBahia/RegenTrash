from .Builder import Builder
from ..Bin import Bin 
from ..Types import Type
from pygame import Vector2
import random
import pygame
from settings.Config import cellSize, screenHeight, screenWidth

class BinBuilder(Builder):

    def __init__(self) -> None:
        self._order = 0
        self.reset()

    def reset(self) -> None:
        self._product = Bin()

    @property
    def product(self) -> Bin:
        product = self._product
        product.list_parts()
        self.reset()
        return product

    def produce_type(self) -> None:
        self._product.add(Type(self._order+1))
        
    def produce_position(self) -> None:
        self._product.add(Vector2(screenWidth*(self._order*2+1)/10, screenHeight*4/5))
        self._order+=1
    
    def produce_speed(self) -> None:
        self._product.add(0)
    
    def produce_sprite(self, sprite) -> None:
        pass
        
    def produce_surface(self) -> None:
        self._product.add(pygame.Surface((cellSize*1, cellSize*1))) 