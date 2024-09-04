from random import randint


def intro(players):
    print("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ")
    check1 = input()
    if (check1 != 'O') and (check1 != 'N'):
        print("Je n'ai pas compris votre réponse")
        return
    players[0] = input("Quel est votre nom (Joueur 1) ? ")
    if (check1 == 'n' or 'N'):
        players[1] = input("Quel est votre nom (Joueur 2) ? ")
        print("Bienvenu ",players[0]," et ",players[1]," nous allons jouer ensemble")
    else:
        players[1] = 0
        print("Bienvenu ",players[0], " nous allons jouer ensemble")
        return players

def play(players):
    pass

def result():
    pass



if (__name__ == "__main__"):
    players = ["", ""]
    intro(players)
    #play(players)