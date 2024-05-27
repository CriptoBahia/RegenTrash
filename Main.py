from settings.Game import Game
from settings.Config import screen, pygame, clock, SCREEN_UPDATE

pygame.init()
mainGame = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGame.gameOver()
        if event.type == SCREEN_UPDATE:
            pass
        if event.type == pygame.KEYDOWN:
            pass
    screen.fill((175,215,70))
    pygame.display.update()
    clock.tick(60)
    