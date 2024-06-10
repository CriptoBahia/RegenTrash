from .Builder import Builder
from ..Trash import Trash 
from ..Type import Type
from pygame import Vector2
from settings.Resolution import Resolution
import random
import pygame

class TrashBuilder(Builder):
    def __init__(self, surface: pygame.surface, cellSize: int) -> None:
        self._cellSize = cellSize
        self._surface = surface
        self.reset()
        self.LEFT_LIMIT = round(surface.get_width()*2/6)
        self.RIGHT_LIMIT = round(surface.get_width()*4/6)
        self.SPEED = 20
        self.DIRECTION = (0, self.SPEED)
        self.COLORS = [(0, 0, 255), (0, 255, 0), (255, 128, 0), (255, 255, 0), (128, 128, 128)]
    
    def reset(self) -> None:
        self._product = Trash(self._surface)

    @property
    def product(self) -> Trash:
        product = self._product
        self.reset()
        return product

    def produce_type(self) -> None:
        self._product.add(random.choice(list(Type)))
        
    def produce_position(self) -> None:
        self.trashX = random.randrange(self.LEFT_LIMIT, self.RIGHT_LIMIT, 45)
        self.trashY = 0
        self._product.add(Vector2(self.trashX, self.trashY))
    
    def produce_speed(self) -> None:
        self._product.add(self.SPEED)
        
    def produce_sprite(self) -> None:
        path = "models/sprites/trashes/"+self._product.parts[0].name+".png"
        sprite = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (self._cellSize, self._cellSize))
        self._product.add(sprite)
        
    def produce_rect(self) -> None:
        self._product.add(self._product.parts[3].get_rect(center=(self.trashX,self.trashY)))
    
    def produce_direction(self) -> None:
        self._product.add(Vector2(self.DIRECTION))