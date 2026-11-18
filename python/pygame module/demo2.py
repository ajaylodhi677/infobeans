import pygame
pygame.init()
#colors
white=(255,255,255)
red =(255,0,0)
black =(0,0,0)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("new try")
screen.fill(white)
pygame.display.update()

#postion
x=45
y=45

exitgame=False

while not exitgame:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitgame=True
pygame.quit()
quit()
