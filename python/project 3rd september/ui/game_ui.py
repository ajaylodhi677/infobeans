import pygame
import os
def createwindow():
    pygame.init()
    screen=pygame.display.set_mode((1200,700))
    pygame.display.set_caption("UNO Game")
    return screen

def loadcardimage(card,size):
    imagepath=os.path.join("assets","cards",card["image"])
    image=pygame.image.load(imagepath)
    image=pygame.transform.scale(image,size)
    return image

def choosecolor(screen):
    font=pygame.font.Font(None,40)
    colors={
        "Red":(220,50,50),
        "Blue":(50,80,220),
        "Green":(50,180,80),
        "Yellow":(220,200,50)
    }
    buttons=[]
    x=150
    for color in colors:
        rect=pygame.Rect(x,350,150,60)
        buttons.append((color,rect))
        x+=200

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return None
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    for color,rect in buttons:
                        if rect.collidepoint(event.pos):
                            return color

        screen.fill((20,100,60))
        text=font.render("Choose Color",True,(255,255,255))
        screen.blit(text,(400,250))

        for color,rect in buttons:
            pygame.draw.rect(screen,colors[color],rect)
            text=font.render(color,True,(255,255,255))
            screen.blit(text,(rect.x+35,rect.y+15))
        pygame.display.update()

def drawgamescreen(screen,currentcard,player,computer,status):
    screen.fill((20,100,60))

    titlefont=pygame.font.Font(None,38)
    font=pygame.font.Font(None,28)
    smallfont=pygame.font.Font(None,24)

    title=titlefont.render("UNO GAME",True,(255,255,255))
    screen.blit(title,(430,20))

    computertext=font.render(
        "Computer Cards: "+str(len(computer["hand"])),
        True,(255,255,255)
    )
    screen.blit(computertext,(50,80))

    currentimage=loadcardimage(currentcard,(120,180))
    screen.blit(currentimage,(440,150))

    currenttext=smallfont.render("Current Card",True,(255,255,255))
    screen.blit(currenttext,(455,335))

    statustext=smallfont.render(status,True,(255,255,255))
    screen.blit(statustext,(50,390))

    playertext=font.render("Ajay",True,(255,255,255))
    screen.blit(playertext,(50,420))

    cardrects=[]
    x=40
    y=460

    for i,card in enumerate(player["hand"]):
        image=loadcardimage(card,(80,120))
        rect=pygame.Rect(x,y,80,120)
        screen.blit(image,rect)
        cardrects.append(rect)
        x+=90

        if x+80>960:
            x=40
            y+=130

    drawbutton=pygame.Rect(1000,370,170,55)
    pygame.draw.rect(screen,(40,40,40),drawbutton)

    drawtext=font.render("DRAW CARD",True,(255,255,255))
    screen.blit(drawtext,(drawbutton.x+20,drawbutton.y+14))

    unobutton=pygame.Rect(700,440,170,55)
    pygame.draw.rect(screen,(180,30,30),unobutton)

    unotext=font.render("UNO!",True,(255,255,255))
    screen.blit(unotext,(unobutton.x+60,unobutton.y+14))

    pygame.display.update()
    return cardrects,drawbutton,unobutton

def getplayeraction(screen,currentcard,player,computer,status):
    while True:
        cardrects,drawbutton,unobutton=drawgamescreen(
            screen,currentcard,player,computer,status
        )
        event=pygame.event.wait()

        if event.type==pygame.QUIT:
            return "quit",None

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                for i,rect in enumerate(cardrects):
                    if rect.collidepoint(event.pos):
                        print("CARD CLICKED:",i)
                        return "play",i

                if drawbutton.collidepoint(event.pos):
                    print("DRAW BUTTON CLICKED")
                    print("MOUSE POSITION:",event.pos)
                    return "draw",None

                if unobutton.collidepoint(event.pos):
                    print("UNO BUTTON CLICKED")
                    return "uno",None
def closewindow():
    pygame.quit()