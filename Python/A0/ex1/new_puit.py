import random


cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )

if cpo != 'O' :
    if cpo != 'N' :
        print("Je n'ai pas compris votre réponse")
elif ():
    n1 = input("Quel est votre nom ? ")
    print("Bienvenu ",n1, " nous allons jouer ensemble \n")
    n2 = 'Machine'
s1 = 0

if cpo == 'N':
    n1 = input("Quel est votre nom ? ")
    print("Bienvenu ",n1, " nous allons jouer ensemble")
    n2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",n2, " nous allons jouer ensemble \n")



np, p2, c = 0, 0, 1
while c == 1:
    c1ok = False
    np += 1
    while c1ok == False :
        print("Joueur ", n1)
        c1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
        c1ok = True
        if c1 != 'pierre' and c1 != 'papier' and c1 != 'ciseaux' and c1 != 'puit': 
            c1ok = False

    if n2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        e2 = ['papier','pierre','ciseaux', 'puit'][random.randint(0, 3)]


    if n2 != 'Machine':
        print("Joueur", n2)
        e2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        while not j2bon :
            print("Joueur ", n2)
            e2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
            j2bon = True
            if e2 != 'pierre' or e2 != 'papier' or e2 != 'ciseaux' or e2 != 'puit': 
                print("Je n'ai pas compris votre réponse")

    #On affiche les choix de chacun
    print("Si on récapitule :",n1, c1, "et", n2, e2,"\n")

    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if c1 == 'papier' and e2 == 'papier' or c1 == 'pierre' and e2 == 'pierre' or c1 == 'ciseaux' and e2 == 'ciseaux' or c1 == 'puit' and e2 == 'puit':
        w12 = "aucun de vous, vous être ex æquo"

    if c1 == 'pierre' and e2 == 'papier' or c1 == 'papier' and e2 == 'ciseaux' or c1 == 'ciseaux' and e2 == 'pierre' or c1 == 'puit' and e2 == 'pierre' or c1 == 'puit' and e2 == 'ciseaux':
        w12 = n2
        p2 = p2 + 1

    if c1 == 'pierre' and e2 == 'ciseaux'  or c1 == 'papier' and e2 == 'pierre' or c1 == 'ciseaux' and e2 == 'papier' or c1 == 'feuille' and e2 == 'puit':
        w12 = n1
        s1 = s1 + 1
        
    #affichage des scores
    print("le gagnant est",w12)
    print("Les scores à l'issue de cette manche sont donc",n1, s1, "et", n2, p2, "\n")

    if np == 5:
        c = False
        
    if np ==1 or np ==2 or np==3 or np==4:
        #On propose de c ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(n1,n2))
        if go == 'N':
            c = False
        else:
            c = True
            print("Vous ne répondez pas à la question, on continue ")
        
if c == False :
    print("Merci d'avoir joué ! A bientôt")