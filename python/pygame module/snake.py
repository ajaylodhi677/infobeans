import pygame
import random
pygame.init()
#colors
white=(255,255,255)
red =(255,0,0)
black =(0,0,0)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Snakeswithajay")
#pygame.display.update()

#Game specific variable
exitgame=False
gameover=False
snakex=45
snakey=45
Snakesize=10
fps=30
velocityx=5
velocityy=0
score=0
foodx=random.randint(20,400)
foody=random.randint(20,300)
clock=pygame.time.Clock()
#game loop
while not exitgame:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitgame=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocityx=5
                velocityy=0
            if event.key==pygame.K_LEFT:
                velocityx=-5
                velocityy=0    
            if event.key==pygame.K_UP:
                velocityy=-5
                velocityx=0    
            if event.key==pygame.K_DOWN:
                velocityy=5 
                velocityx=0    

    snakex+=velocityx
    snakey+=velocityy 
    if abs(snakex-foodx)<10 and abs(snakey-foody)<10:
        score+=1
       # Snakesize+=10
        print("score :",score)
        foodx=random.randint(20,400)
        foody=random.randint(20,300)                              
    screen.fill(white)
    pygame.draw.rect(screen,black,[snakex,snakey,Snakesize,Snakesize])
    pygame.draw.rect(screen,red,[foodx,foody,10,10])
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
quit()            