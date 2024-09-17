

def mot_nlettres(lst_mot:list, n:int)->list:
    lst = []
    
    for e in lst_mot:
        if (len(e) == n):
            lst.append(e)
    return lst

def test():
    LST = ["bonjour", "jour", "nuit", "qqqqq", "test", "bonnuit", "bon"]
    assert mot_nlettres(LST, 4) == ["jour", "nuit", "test"]
    assert mot_nlettres(LST, 5) == ["qqqqq"]
    assert mot_nlettres(LST, 7) == ["bonjour", "bonnuit"]
    assert mot_nlettres(LST, 0) == []
    assert mot_nlettres([], 4) == []
    
def commence_par(mot:str, prefixe:str)->bool:
    for i in range(len(prefixe)):
        if (mot[i] != prefixe[i]):
            return False
    return True

def finit_par(mot:str, suffixe:str)->bool:
    mot_len = len(mot)
    
    for i in range(1, len(suffixe)+1):
        if (mot[mot_len-i] != suffixe[-i]):
            return False
    return True

def finissent_par(lst_mot:list, suffixe:str)->list:
    lst = []
    
    for e in lst_mot:
        if (finit_par(e, suffixe)):
            lst.append(e)
    return lst

def commencent_par(lst_mot:list, prefixe:str)->list:
    lst = []
    
    for e in lst_mot:
        if (commence_par(e, prefixe)):
            lst.append(e)
    return lst

def liste_mots(lst_mot:list, prefixe:str, suffixe:str, n:int)->list:
    lst = mot_nlettres(lst_mot, n)
    res = []
    
    for e in lst:
        if (commence_par(e, prefixe) and finit_par(e, suffixe)):
            res.append(e)
    return res

def dictionnaire(filename:str)->str:
    lst_mot = []
    line = ""
    
    with open(filename, "r") as file:   #calls __exit__ when out of scope
        line = file.readline()
        while (line != ""):
            lst_mot.append(line)
            line = file.readline()
    return lst_mot

if (__name__ == "__main__"):
    LST = ["bonjour", "jour", "nuit", "qqqqq", "test", "bonnuit", "bon", "pretestsuf"]
    #test()
    #print(liste_mots(LST, "", "", 3))
    print(dictionnaire("qwerty.txt"))
    
    pass