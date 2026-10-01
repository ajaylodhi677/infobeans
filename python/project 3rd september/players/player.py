def createplayer(name):
    player={
        "name":name,
        "hand":[],
        "score":0
    }
    return player

def addcard(player,card):
    player["hand"].append(card)

def removecard(player,cardindex):
    card=player["hand"].pop(cardindex)
    return card

def showhand(player):
    print("\nPlayer:",player["name"])
    print("Cards:")
    for i,card in enumerate(player["hand"]):
        print(i+1,card["color"],card["value"])