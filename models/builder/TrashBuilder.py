from .Builder import Builder
from ..Trash import Trash 
from ..Types import Type
from pygame import Vector2
import random
import pygame
from settings.Config import cellSize

class TrashBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Trash()

    @property
    def product(self) -> Trash:
        product = self._product
        product.list_parts()
        self.reset()
        return product

    def produce_type(self) -> None:
        self._product.add(random.choice(list(Type)))
        
    def produce_position(self) -> None:
        self._product.add(Vector2(random.randrange(300, 600, 1), 0))
    
    def produce_speed(self) -> None:
        self._product.add(20)
    
    def produce_sprite(self, sprite) -> None:
        pass
        
    def produce_surface(self) -> None:
        self._product.add(pygame.Surface((cellSize*1, cellSize*1))) 