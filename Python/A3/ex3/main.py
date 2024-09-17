from random import randint as rdi

def places_lettre(char:str, MOT:str)->list:
    res = []
    for i in range(len(MOT)):
        if (char == MOT[i]):
            res.append(i)
    return res

def output_str(mot:str, char_pos:list)->str:
    output = list("_" * len(mot))
    for e in char_pos:
        output[e] = list(mot)[e]
    return "".join(output)

def buildlist(FILENAME:str)->list:
    lst_mot = []
    
    with open(FILENAME, 'r') as F:
        txt = F.readlines()
    lst_mot = "".join(txt).lower().split(", ")
    
    return lst_mot

def builddict(lst_mot:list)->dict:
    dictio = {}
    
    for e in lst_mot:
        len_mot = len(e)
        if (len_mot not in dictio.keys()):
            dictio.update({len_mot : []})
        
        lst = list(dictio.get(len_mot))
        lst.append(str(e))
        dictio.update({len_mot: lst})
        
    return dictio
    
def select_word(sorted_word:dict, word_len:int)->str:
    length = len(sorted_word.get(word_len))
    print(length)
    return sorted_word[word_len][rdi(0, length)]

def run_game(FILE:str):
    DICT_MOT = builddict(buildlist(FILE))
    MAX_GUESS = 5
    PENDU = ("|---]","|  O ","| 'T'","| / \\","L____")
    DIFFICULTY = ("easy", "medium", "hard")
    
    guess = MAX_GUESS
    user_guess = ""
    guessed = []
    
    difficulty_flag = True
    flag = True
    found = False
    
    
    while difficulty_flag:
        print("Veuillez choisir la difficulte:\n- easy\n- medium\n- hard\n")
        user_diff = input()
        difficulty_flag = False
        if (user_diff == DIFFICULTY[0]):
            _random = (4, 6)
        elif (user_diff == DIFFICULTY[1]):
            _random = (7, 8)
        elif (user_diff == DIFFICULTY[2]):
            _random = (9, 20)
        else:
            print("Veuillez indiquer une difficulte valide")
            difficulty_flag = True
        
        while flag and not difficulty_flag:
            try:
                MOT = select_word(DICT_MOT, rdi(_random[0], _random[1]))
                flag = False
            except: #aucun mots de la longueur choisi
                pass
            
    while guess:
        print(output_str(MOT, guessed))
        if (user_guess == MOT or len(guessed) == len(MOT)):
            guess = 0
            print("Vous avez gagne! Le mot etait {0}".format(MOT))
            found = True
            return

        user_guess = input("Choisissez une lettre ou devinez le mot: ")
        if (user_guess[0] not in guessed):
            placed = places_lettre(user_guess[0], MOT)
        
        if (len(placed) == 0):
            guess -= 1
            print("pas de chance, il reste {0} chance(s)".format(guess))
            for i in range(5 - guess):
                print(PENDU[i])
        else:
            for e in placed:
                guessed.append(e)
            print("Bien joue, il reste {0} chance(s)".format(guess))
        
        
        
    if (not found):
        print("Perdu, le mot etait {0}".format(MOT))
    



if (__name__ == "__main__"):
    #print(places_lettre("q", "maman"))
    #print(output_str("bonjour", [0, 2, 6]))
    run_game("buildlist.txt")
    #builddict(buildlist("buildlist.txt"))
    pass