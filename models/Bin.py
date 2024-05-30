from settings.Config import SCREEN

class Bin:
    
    def __init__(self):
        self.parts = []   
        
    def add(self, part: any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        for i in self.parts:
            print(i)
        
    def draw(self):
        SCREEN.blit(self.parts[3], (self.parts[1].x, self.parts[1].y))
    
    def store(self, trash) -> int:
        if trash.parts[0] == self.parts[0]:
            score = 10
        else:
            score = -10
        trash.die()
        return score