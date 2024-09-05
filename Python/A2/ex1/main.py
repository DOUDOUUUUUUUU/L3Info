from math import inf


def somme1(lst:list)->int:
    '''renvoie la somme de la liste lst'''
    res = 0
    for i in lst:
        res += i
    return res

def somme2(lst:list)->int:
    '''renvoie la somme de la liste lst'''
    res = 0
    for i in range(len(lst)):
        res = res + lst[i]
    return res

def somme3(lst:list)->int:
    '''renvoie la somme de la liste lst'''
    res = 0
    max = len(lst)
    i = 0
    while i < max:
        res += lst[i]
        i += 1
    return res

def test_exercice1():
    '''straightforward'''
    print("TEST SOMME")
    print("Test liste vide: ", somme3([]))
    list1 = [1, 10, 100, 1000, 10000]
    print("Test somme 11111: ", somme3(list1))






def moyenne(lst:list)->float:
    '''renvoie la moyenne de la liste lst'''
    moy = 0
    max = len(lst)
    
    for i in lst:
        moy += i
    if (max):
        moy /= max
    return moy

def test_exercice2():
    '''straightforward'''
    print("TEST MOYENNE")
    print("Test liste vide: ", moyenne([]))
    list1 = [0, 23, 40, 10, 30, 25, 15, 17]
    print("Test moyenne 20: ", moyenne(list1))







def nb_sup1(lst:list, e:int)->int:
    '''renvoie le nombre d'element superieur a e dans la liste lst'''
    n = 0
    for i in range(len(lst)):
        if (lst[i] > e):
            n += 1
    return n

def nb_sup2(lst:list, e:int)->int:
    '''renvoie le nombre d'element superieur a e dans la liste lst'''
    n = 0
    for i in lst:
        if (i > e):
            n += 1
    return n

def test_exercice3():
    '''straightforward'''
    print("TEST nb_sup")
    print("Test liste vide: ", nb_sup2([], 20))
    list1 = [0, 23, 40, 10, 30, 25, 15, 17]
    print("Test nb_sup 20: ", nb_sup2(list1, 20))
    



def moy_sup(lst:list, e:int)->float:
    '''renvoie la moyenne des elements superieurs a e de la liste lst'''
    nb_above = []
    for i in lst:
        if (i > e):
            nb_above.append(i)
    print(nb_above)
    return moyenne(nb_above)

def test_exercice4():
    '''straightforward'''
    print("TEST moy_sup")
    print("Test liste vide: ", moy_sup([], 20))
    list1 = [0, 23, 40, 10, 30, 25, 15, 17]
    print("Test moy_sup 20 (resultat = 29.5): ", moy_sup(list1, 20))






def val_max(lst:list)->int:
    '''retourne la valeur max de la liste'''
    max = -inf
    if (not len(lst)):
        return 0
    for i in lst:
        if (i > max):
            max = i
    return max

def test_exercice5():
    '''straightforward'''
    print("TEST val_max")
    print("Test liste vide: ", val_max([]))
    list1 = [0, 23, 40, 10, 30, 25, 15, 17]
    print("Test moy_sup 40: ", val_max(list1))




def ind_max(lst:list)->int:
    '''retourne l'indice de l'element maximal de la liste lst'''
    id_max = 0
    for i in range(len(lst)):
        if (lst[id_max] < lst[i]):
            id_max = i
    return id_max

def test_exercice6():
    '''straightforward'''
    print("TEST ind_max")
    print("Test liste vide: ", ind_max([]))
    list1 = [0, 23, 40, 10, 30, 25, 15, 17]
    print("Test ind_max 40 (resultat = 2): ", ind_max(list1))


if (__name__ == "__main__"):
    #test_exercice1()
    #test_exercice2()
    #test_exercice3()
    #test_exercice4()
    #test_exercice5()
    test_exercice6()