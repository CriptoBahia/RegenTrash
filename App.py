from settings.Game import Game
from settings.State import State
from settings.Config import Config, pygame
from settings.Resolution import Resolution

gameState = State.RUNNING

pygame.init()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
CLOCK = pygame.time.Clock()
FPS = 60

config = Config(Resolution.SVGA)
mainGame = Game(config)


def run(eventType):
    if eventType == pygame.KEYDOWN or eventType == pygame.KEYUP:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
                return State.PAUSED
        else:
            mainGame.input(eventType, keys)
    mainGame.surface.fill((175,215,70))
    mainGame.draw()
    return State.RUNNING

def pause(eventType):
    if eventType == pygame.KEYDOWN or eventType == pygame.KEYUP:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
                return State.RUNNING
    largeText = pygame.font.SysFont("comicsansms",115)
    textSurface = largeText.render("Paused", True, (0,0,0))
    TextRect = textSurface.get_rect()
    TextRect.center = ((config.screenWidth/2),(config.screenheight/2))
    config.screen.blit(textSurface, TextRect)
    mainGame.last_build = pygame.time.get_ticks()
    return State.PAUSED
    

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame.gameOver()
            if event.type == SCREEN_UPDATE and gameState == State.RUNNING:
                mainGame.update()
            match gameState: 
                case State.RUNNING:
                    gameState = run(event.type)
                case State.PAUSED:
                    #gameState = pause(event.type)
                    pass
    pygame.display.update()
    CLOCK.tick(FPS)