import pygame
pygame.init()
#colors
white=(255,255,255)
red =(255,0,0)
black =(0,0,0)
screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Snakeswithajay")
#pygame.display.update()

#Game specific variable
exitgame=False
gameover=False
snakex=45
snakey=45
Snakesize=10
fps=30
velocityx=2
velocityy=2

clock=pygame.time.Clock()
#game loop
while not exitgame:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitgame=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snakex=snakex+10
            if event.key==pygame.K_LEFT:
                snakex=snakex-10    
            if event.key==pygame.K_UP:
                snakey=snakey-10    
            if event.key==pygame.K_DOWN:
                snakey=snakey+10 
    snakex+=velocityx
    snakey+=velocityy                               
    screen.fill(white)
    pygame.draw.rect(screen,black,[snakex,snakey,Snakesize,Snakesize])
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
quit()            