from settings.Game import Game
from settings.States import State
from settings.Config import SCREEN, pygame, CLOCK, SCREEN_UPDATE, FPS, SCREENHEIGHT, SCREENWIDTH

gameState = State.RUNNING
pygame.init()
mainGame = Game()

def run(eventType):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
            print("Paused")
            return State.PAUSED
    if eventType == pygame.KEYDOWN or eventType == pygame.KEYUP:
            mainGame.input(eventType, keys)
            print(eventType)
    SCREEN.fill((175,215,70))
    mainGame.draw()
    return State.RUNNING

def pause(event):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
            print("Unpaused")
            return State.RUNNING
    largeText = pygame.font.SysFont("comicsansms",115)
    textSurface = largeText.render("Paused", True, (0,0,0))
    TextRect = textSurface.get_rect()
    TextRect.center = ((SCREENWIDTH/2),(SCREENHEIGHT/2))
    SCREEN.blit(textSurface, TextRect)
    return State.PAUSED
    

while True:
    print(gameState)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame.gameOver()
            if event.type == SCREEN_UPDATE and gameState == State.RUNNING:
                mainGame.update()
            match gameState: 
                case State.RUNNING:
                    gameState = run(event.type)
                case State.PAUSED:
                    gameState = pause(event)
    pygame.display.update()
    CLOCK.tick(FPS)
    
    
def pause():

    largeText = pygame.font.SysFont("comicsansms",115)
    textSurface = largeText.render("Paused", True, (0,0,0))
    TextRect = textSurface.get_rect()
    TextRect.center = ((SCREENWIDTH/2),(SCREENHEIGHT/2))
    SCREEN.blit(textSurface, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)  