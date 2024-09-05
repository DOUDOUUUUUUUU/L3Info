

def position1(lst:list, elt:int)->int:
    '''retourne l'index de elt dans lst, renvoie -1 si elt n'est pas dans lst'''
    for i in range(len(lst)):
        if (lst[i] == elt):
            return i
    return -1

def position2(lst:list, elt:int)->int:
    '''retourne l'index de elt dans lst, renvoie -1 si elt n'est pas dans lst'''
    i = 0
    while i != len(lst):
        if (lst[i] == elt):
            return i
        i += 1
    return -1

def testpos(liste:list):
    print(position1(liste, 42)) # 5
    print(position1(liste, 41)) # -1
    print(position2(liste, 0))  # 11
    print(position2(liste, 2))  # -1



def nb_occurrences(lst:list, e:int)->int:
    '''retourne le nombre d'occurence du nombre e dans la liste lst'''
    nb_occur = 0
    for i in lst:
        if (i == e):
            nb_occur += 1
    return nb_occur

def testoccurrence(liste1:list, liste2:list):
    print(nb_occurrences(liste1, 42)) # 1
    print(nb_occurrences(liste1, 41)) # 0
    print(nb_occurrences(liste2, 1))  # 2
    print(nb_occurrences(liste2, 12)) # 4



def est_triee1(lst:list)->bool:
    '''renvoie 1 si la liste est triee, 0 sinon'''
    for i in range(1, len(lst)):
        if (lst[i-1] > lst[i]):
            return False
    return True

def est_triee2(lst:list)->bool:
    '''renvoie 1 si la liste est triee, 0 sinon'''
    i = 1
    while (lst[i-1] < lst[i]):
        if (i + 1 > len(lst)):
            return True
    return False

def position_tri(lst:list, e:int):
    start = 0
    end = len(lst) -1
    while (start <= end):
        mid = (start + end) // 2
        print(start, end, mid, sep=' ')
        if (lst[mid] == e):
            return mid
        elif (lst[mid] < e):
            start = mid+1
        else:
            end = mid-1
    return -1


def a_repetition(lst:list):
    cache = []
    i = 0
    while i < len(lst):
        if (lst[i] in cache):
            print(lst[i])
            return True
        cache.append(lst[i])
        i += 1
    return False

if (__name__ == "__main__"):
    liste1 = [1, 54, 654 ,7653, 87, 42 , 7654, 21, 875, 9087, 43 ,0 , 876]
    liste2 = [1, 543 ,765, 12, 1, 65 ,32, 865, 2642, 12, 12, 12, 65, 0, 6]
    liste3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    #testpos(liste1)
    #testoccurrence(liste1, liste2)
    #print(position_tri(liste3, 22))
    print(a_repetition(liste1))
    
    