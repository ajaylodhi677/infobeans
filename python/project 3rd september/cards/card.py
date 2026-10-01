import random
def createcard(color,value,cardtype,image):
    card={
        "color":color,
        "value":value,
        "type":cardtype,
        "image":image
    }
    return card
def createdeck():
    deck=[]
    colors=["Blue","Green","Red","Yellow"]
#================== 0 =================
    for color in colors:
        card=createcard(color,0,"number",f"{color}_0.png")
        deck.append(card)
#================== numbers cards =================
        for number in range(1,10):
            for i in range(2):
                card=createcard(
                    color,
                    number,
                    "number",
                    f"{color}_{number}.png"
                )
                deck.append(card)
#================== action cards =================
        actions={
            "Skip":"Skip",
            "Reverse":"Reverse",
            "Draw Two":"Draw_2"
        }
        for action,image in actions.items():
            for i in range(2):
                card=createcard(
                    color,
                    action,
                    "action",
                    f"{color}_{image}.png"
                )
                deck.append(card)
#================== Wild color cards =================
    for i in range(4):
        card=createcard(
            None,
            "Wild",
            "wild",
            "Wild_Card_Change_Colour.png"
        )
        deck.append(card)
#================== Wild +4 card =================
    for i in range(4):
        card=createcard(
            None,
            "Wild Draw Four",
            "wild",
            "Wild_Card_Draw_4.png"
        )
        deck.append(card)
    random.shuffle(deck)
    return deck