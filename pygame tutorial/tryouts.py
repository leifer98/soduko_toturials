import pygame

pygame.init()

black, white, red, green, blue = (0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(white)

pixArray = pygame.PixelArray(gameDisplay)
pixArray[10][10] = green

pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
pygame.draw.rect(gameDisplay,red,(400,400,50,50))
pygame.draw.circle(gameDisplay, black, (150,150), 75)
pygame.draw.polygon(gameDisplay, green, ((150,150), (400,200),(300,250),(450,500)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()