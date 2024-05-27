from settings.Game import Game
from settings.Config import screen, pygame, clock, SCREEN_UPDATE, fps

pygame.init()
mainGame = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGame.gameOver()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            mainGame.input(event.key)
    mainGame.draw()
    pygame.display.update()
    screen.fill((175,215,70))
    clock.tick(fps)
    