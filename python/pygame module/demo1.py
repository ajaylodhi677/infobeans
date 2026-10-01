import pygame
pygame.init()
#creating window 
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("THis is my first window")

#Game specific variable
exitgame=False
gameover=False

#Creating a game loop
while not exitgame:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitgame=True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right key")   

pygame.quit()
quit() 