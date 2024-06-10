import pygame
from .Resolution import Resolution

class Config:
    def __init__(self, resolution: Resolution) -> None:
        self._XCELLNUMBER = 20
        self._YCELLNUMBER = 12 
        self.setResolution(resolution)
    
    @property
    def surface(self) -> pygame.Surface:
        return self._surface
    
    @property
    def cellSize(self) -> int:
        return self._cellSize
    @cellSize.setter
    def cellSize(self, cellSize: int):
        self._cellSize = cellSize
        
    def setResolution(self, resolution: Resolution) -> None:
        match resolution:
            case Resolution.VGA:
                self._cellSize = 32
            case Resolution.SVGA:
                self._cellSize = 40
            case Resolution.XGA:
                self._cellSize = 51
            case Resolution.HD:
                self._cellSize = 64
            case Resolution.FULLHD:
                self._cellSize = 96   
            case _:
                self._cellSize = 51
        surfaceWidth =self._cellSize*self._XCELLNUMBER
        surfaceheight= self._cellSize*self._YCELLNUMBER
        self._surface = pygame.display.set_mode((surfaceWidth, surfaceheight), pygame.FULLSCREEN)
        
        
        
