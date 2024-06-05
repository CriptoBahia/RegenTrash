from .Builder import Builder
from ..Trash import Trash 
from ..Types import Type
from pygame import Vector2
import random
import pygame
from settings.Config import CELLSIZE

LEFT_LIMIT = 320
RIGHT_LIMIT = 580
SPEED = 20
DIRECTION = (0, SPEED)
COLORS = [(0, 0, 255), (0, 255, 0), (255, 128, 0), (255, 255, 0), (128, 128, 128)]

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
        self.trashX = random.randrange(LEFT_LIMIT, RIGHT_LIMIT, 40)
        self.trashY = 0
        self._product.add(Vector2(self.trashX, self.trashY))
    
    def produce_speed(self) -> None:
        self._product.add(SPEED)
    def produce_sprite(self) -> None:
        path = "models/sprites/trashes/"+self._product.parts[0].name+".png"
        print(path)
        print(pygame.image.load(path).convert_alpha())
        self._product.add(pygame.image.load(path).convert_alpha())
        
    def produce_surface(self) -> None:
        pass
        """self._product.add(pygame.Surface((CELLSIZE, CELLSIZE)))
        match self._product.parts[0]:
            case Type.PAPER:
                self._product.parts[3].fill(COLORS[0])
            case Type.GLASS:
                self._product.parts[3].fill(COLORS[1])
            case Type.PLASTIC:
                self._product.parts[3].fill(COLORS[2])
            case Type.METAL:
                self._product.parts[3].fill(COLORS[3])
            case Type.ORGANIC:
                self._product.parts[3].fill(COLORS[4])"""
        
    def produce_rect(self) -> None:
        self._product.add(self._product.parts[3].get_rect(center=(self.trashX,self.trashY)))
    
    def produce_direction(self) -> None:
        self._product.add(Vector2(DIRECTION))