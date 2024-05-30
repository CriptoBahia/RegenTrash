from .Builder import Builder
from ..Trash import Trash 
from ..Types import Type
from pygame import Vector2
import random
import pygame
from settings.Config import cellSize

LEFT_LIMIT = 320
RIGHT_LIMIT = 580
SPEED = 20
DIRECTION = (0, SPEED)

class TrashBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Trash()

    @property
    def product(self) -> Trash:
        product = self._product
        self.reset()
        return product

    def produce_type(self) -> None:
        self._product.add(random.choice(list(Type)))
        
    def produce_position(self) -> None:
        self._product.add(Vector2(random.randrange(LEFT_LIMIT, RIGHT_LIMIT, 80), 0))
    
    def produce_speed(self) -> None:
        self._product.add(SPEED)
    def produce_sprite(self, sprite) -> None:
        pass
        
    def produce_surface(self) -> None:
        self._product.add(pygame.Surface((cellSize, cellSize))) 
        
    def produce_direction(self) -> None:
        self._product.add(Vector2(DIRECTION))