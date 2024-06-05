from settings.Game import Game
from settings.Config import SCREEN, pygame, CLOCK, SCREEN_UPDATE, FPS

pygame.init()
mainGame = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGame.gameOver()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            mainGame.input(event.type, event.key)
    SCREEN.fill((175,215,70))
    mainGame.draw()
    pygame.display.update()
    CLOCK.tick(FPS)
    