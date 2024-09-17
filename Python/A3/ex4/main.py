
def mot_correspond(mot:str, motif:str)->bool:
    try:
        assert len(mot) == len(motif)
    except:
        raise ValueError
    
    if (mot == motif):
        return True
    
    for i in range(len(mot)):
        if (motif[i] != '.' and mot[i] != motif[i]):
            return False
    
    return True

def presente(lettre:str, mot:str)->int:
    try:
        assert len(lettre) == 1
        assert len(mot) > 0
    except:
        raise ValueError
    
    for i in range(len(mot)):
        if (mot[i] == lettre):
            return i
    return -1

def mot_possible(mot:str, set_lettre:str)->bool:
    match = 0
    lst_lettre = list(set_lettre)
    for e in list(mot):
        if (e in lst_lettre):
            match += 1
            lst_lettre.remove(e)
    if (match == len(mot)):
        return True
    return False



def mot_nlettres(lst_mot:list, n:int)->list:
    lst = []
    
    for e in lst_mot:
        if (len(e) == n):
            lst.append(e)
    return lst

def dictionnaire(filename:str)->str:
    lst_mot = []
    line = ""
    
    with open(filename, "r") as file:   #calls __exit__ when out of scope
        line = file.readline()
        while (line != ""):
            lst_mot.append(line.strip())
            line = file.readline()
    return lst_mot

def mot_optimaux(dico:list, lettres:str)->list:
    lst_lettre = list(lettres)
    mot_len_max = 0
    mot = []
    for e in dico:
        mot_len = len(e)
        if (mot_possible(e, lst_lettre)):
            
            if (mot_len > mot_len_max):
                mot = [e]
                mot_len_max = mot_len
            elif (mot_len == mot_len_max):
                mot.append(e)
    return mot

if (__name__ == "__main__"):
    #print(mot_possible("yy", "qwerty"))
    URL = "littre.txt"
    print(mot_optimaux(dictionnaire(URL), "gdbfuiqdqofdqwvcucbiegfyofeqp"))
    pass