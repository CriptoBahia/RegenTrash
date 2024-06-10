import pygame
from .Resolution import Resolution

SCREEN = screen

class Config:
    def __init__(self) -> None:
        self.screen = None
        self.screenWidth = None
        self.screenheight = None
        self.XCELLNUMBER = 20
        self.YCELLNUMBER = 12
        self._resolution = None
        pass
    
    @property
    def resolution(self) -> Resolution:
        return self._resolution

    @resolution.setter
    def resolution(self, resolution= Resolution.HD) -> None:
        match resolution:
            case Resolution.VGA:
                self.cellSize = 32
            case Resolution.SVGA:
                self.cellSize = 40
            case Resolution.XGA:
                self.cellSize = 51
            case Resolution.HD:
                self.cellSize = 64
            case Resolution.HD:
                self.cellSize = 96    
        self._resolution = resolution
        global SCREENWIDTH
        global SCREENHEIGHT
        SCREENWIDTH = self.cellSize*self.XCELLNUMBER
        self.screenWidth = SCREENWIDTH
        SCREENHEIGHT= self.cellSize*self.YCELLNUMBER
        self.screenheight = SCREENHEIGHT
        
    def apply(self):
        global screen 
        screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.screen = screen
        
