def somme_recursive(lst:list)->int:
    """ additionne tout les  nombres de la liste de maniere recursive """
    if (len(lst) == 1):
        return lst[0]
    else:
        return lst[0] + somme_recursive(lst[1:])
    

def rec_factorial(n:int)->int:
    """ retourne le factoriel du nombre de maniere recursive """
    if (n in [0, 1]):
        return 1
    return n * rec_factorial(n-1)

def rec_longueur(lst:list, res:int=0)->int:
    """ renvoi la longueur de l'array de maniere recursive """
    if (lst == []):
        return res
    return rec_longueur(lst.pop(), res+1)

def rec_minimum(lst:list, min:int=999)->int:
    """ renvoi le minimun d emaniere recursive """
    
    return rec_minimum(lst[1:], min)

def rec_liste_pair(lst:list, pairs:list=[])->list:
    if (lst == []):
        return pairs
    if (not lst[0] % 2):
        pairs.append(lst[0])
    return rec_liste_pair(lst[1:], pairs)

def concat_list(lst:list)->list:
    
    return


def incluse(lst1:list, lst2:list)->bool:
    if not lst1:
        return True
    if len(lst2) < len(lst1) or lst1[0] not in lst2:
        return False
    return incluse(lst1[1:], lst2[(lst2.index(lst1[0]) + 1):])

if (__name__ == "__main__"):
    print(rec_liste_pair([]))
    pass