import random
import datetime
import pygame
from cards.card import createdeck
from players.player import createplayer,addcard,removecard
from ui.game_ui import createwindow,getplayeraction,choosecolor,drawgamescreen,closewindow

def isvalidcard(card,currentcard):
    if card["type"]=="wild":
        return True
    if card["color"]==currentcard["color"]:
        return True
    if card["value"]==currentcard["value"]:
        return True
    return False

def canplaywilddrawfour(card,player,currentcard):
    if card["value"]!="Wild Draw Four":
        return True
    currentcolor=currentcard["color"]
    for playercard in player["hand"]:
        if playercard["type"]!="wild":
            if playercard["color"]==currentcolor:
                return True
    return True

def isplayable(card,player,currentcard):
    if card["value"]=="Wild Draw Four":
        return canplaywilddrawfour(card,player,currentcard)
    return isvalidcard(card,currentcard)

def refilldrawpile(drawpile,discardpile):
    if len(drawpile)==0:
        if len(discardpile)>1:
            currentcard=discardpile[-1]
            drawpile.extend(discardpile[:-1])
            discardpile.clear()
            discardpile.append(currentcard)
            random.shuffle(drawpile)

def drawcard(player,drawpile,discardpile):
    if len(drawpile)==0:
        refilldrawpile(drawpile,discardpile)
    if len(drawpile)==0:
        return None
    card=drawpile.pop()
    addcard(player,card)
    return card

def drawcardsforplayer(player,count,drawpile,discardpile):
    cards=[]
    for i in range(count):
        card=drawcard(player,drawpile,discardpile)
        if card is not None:
            cards.append(card)
    return cards

def choosecomputercolor():
    colors=["Red","Blue","Green","Yellow"]
    return random.choice(colors)

def getspecialaction(card):
    if card["value"]=="Skip":
        return "skip"
    if card["value"]=="Reverse":
        return "reverse"
    if card["value"]=="Draw Two":
        return "draw_two"
    if card["value"]=="Wild":
        return "wild"
    if card["value"]=="Wild Draw Four":
        return "wild_draw_four"
    return "normal"

def computerturn(computer,player,currentcard,drawpile,discardpile):
    playable=[]
    for i,card in enumerate(computer["hand"]):
        if isplayable(card,computer,currentcard):
            playable.append((i,card))

    if len(playable)==0:
        card=drawcard(computer,drawpile,discardpile)
        if card is None:
            return currentcard,"draw_none"

        print("Computer had no valid card.")
        print("Computer Draws:",card)

        if isplayable(card,computer,currentcard):
            i=len(computer["hand"])-1
            card=removecard(computer,i)
            print("Computer Played Drawn Card:",card)
            discardpile.append(card)
            currentcard=card

            if card["type"]=="wild":
                color=choosecomputercolor()
                card["color"]=color
                print("Computer chose:",color)

            return currentcard,getspecialaction(card)

        return currentcard,"draw"

    i,card=random.choice(playable)
    card=removecard(computer,i)
    print("Computer Played:",card)
    discardpile.append(card)
    currentcard=card

    if card["type"]=="wild":
        color=choosecomputercolor()
        card["color"]=color
        print("Computer chose:",color)

    return currentcard,getspecialaction(card)

def showwinner(player,computer):
    print()
    print("====================")
    print("       GAME OVER fat gyi na")
    print("====================")

    if len(player["hand"])==0:
        print("Winner:",player["name"])
    elif len(computer["hand"])==0:
        print("Winner:",computer["name"])

    print("Player Cards:",len(player["hand"]))
    print("Computer Cards:",len(computer["hand"]))

def showcomputercard(screen,currentcard,player,computer,status):
    drawgamescreen(screen,currentcard,player,computer,status)
    pygame.time.delay(1000)

def startgame():
    screen=createwindow()
    gametime=datetime.datetime.now()
    print("Game Started:",gametime.strftime("%d-%m-%Y %H:%M:%S"))

    deck=createdeck()
    player=createplayer("Ajay")
    computer=createplayer("Computer")

    drawpile=deck
    discardpile=[]

    for i in range(7):
        addcard(player,drawpile.pop())

    for i in range(7):
        addcard(computer,drawpile.pop())

    currentcard=drawpile.pop()

    while currentcard["type"]=="wild":
        drawpile.insert(0,currentcard)
        random.shuffle(drawpile)
        currentcard=drawpile.pop()

    discardpile.append(currentcard)
    turn=0
    status="Your Turn"

    while True:
        if len(player["hand"])==0:
            showwinner(player,computer)
            status="You Win!"
            drawgamescreen(screen,currentcard,player,computer,status)
            pygame.time.delay(2000)
            break

        if len(computer["hand"])==0:
            showwinner(player,computer)
            status="Computer Wins!"
            drawgamescreen(screen,currentcard,player,computer,status)
            pygame.time.delay(2000)
            break

        if turn==0:
            status="Your Turn"
            action,value=getplayeraction(
                screen,currentcard,player,computer,status
            )

            if action=="quit":
                break

            if action=="draw":
                print("PLAYER DRAW ACTION RECEIVED")
                card=drawcard(player,drawpile,discardpile)

                if card is not None:
                    print("Card Drawn:",card)
                    status="You drew a card."

                    if isplayable(card,player,currentcard):
                        status="Drawn card is playable."

                turn=1
                continue

            if action=="uno":
                if len(player["hand"])==1:
                    print("UNO!")
                    status="UNO called!"
                else:
                    print("UNO can only be called with 1 card.")
                    status="You can call UNO with 1 card."
                continue

            if action=="play":
                i=value

                if i<0 or i>=len(player["hand"]):
                    continue

                card=player["hand"][i]

                if not isplayable(card,player,currentcard):
                    print("Invalid Card!")
                    status="Invalid Card! Choose another card."
                    continue

                card=removecard(player,i)
                discardpile.append(card)
                currentcard=card
                print("You Played:",card)

                if card["type"]=="wild":
                    color=choosecolor(screen)

                    if color is None:
                        break

                    card["color"]=color
                    print("You chose:",color)

                specialaction=getspecialaction(card)

                if len(player["hand"])==1:
                    print("UNO!")
                    status="UNO! You have 1 card left."

                if len(player["hand"])==0:
                    continue

                if specialaction=="skip":
                    print("You played Skip!")
                    status="Skip! Your turn again."
                    turn=0

                elif specialaction=="reverse":
                    print("You played Reverse!")
                    status="Reverse! Your turn again."
                    turn=0

                elif specialaction=="draw_two":
                    print("You played Draw Two!")
                    drawcardsforplayer(
                        computer,2,drawpile,discardpile
                    )
                    print("Computer Draw Two!")
                    status="Computer draws 2 cards. Your turn again."
                    turn=0

                elif specialaction=="wild":
                    print("You played Wild!")
                    status="Wild! Your turn again."
                    turn=0

                elif specialaction=="wild_draw_four":
                    print("You played Wild Draw Four!")
                    drawcardsforplayer(
                        computer,4,drawpile,discardpile
                    )
                    print("Computer Draw Four!")
                    status="Computer draws 4 cards. Your turn again."
                    turn=0

                else:
                    turn=1

        else:
            status="Computer's Turn"
            currentcard,specialaction=computerturn(
                computer,player,currentcard,drawpile,discardpile
            )

            if len(computer["hand"])==1:
                print("Computer: UNO!")
                status="Computer: UNO!"

            if len(computer["hand"])==0:
                continue

            if specialaction=="skip":
                print("Computer played Skip!")
                status="Computer played Skip! Computer's turn again."
                showcomputercard(
                    screen,currentcard,player,computer,status
                )
                turn=1

            elif specialaction=="reverse":
                print("Computer played Reverse!")
                status="Computer played Reverse! Computer's turn again."
                showcomputercard(
                    screen,currentcard,player,computer,status
                )
                turn=1

            elif specialaction=="draw_two":
                drawcardsforplayer(
                    player,2,drawpile,discardpile
                )
                print("Computer Draw Two!")
                status="You draw 2 cards. Computer's turn again."
                showcomputercard(
                    screen,currentcard,player,computer,status
                )
                turn=1

            elif specialaction=="wild":
                print("Computer played Wild!")
                status="Computer played Wild. Computer's turn again."
                showcomputercard(
                    screen,currentcard,player,computer,status
                )
                turn=1

            elif specialaction=="wild_draw_four":
                drawcardsforplayer(
                    player,4,drawpile,discardpile
                )
                print("Computer Draw Four!")
                status="You draw 4 cards. Computer's turn again."
                showcomputercard(
                    screen,currentcard,player,computer,status
                )
                turn=1

            else:
                turn=0

    closewindow()

if __name__=="__main__":
    startgame()