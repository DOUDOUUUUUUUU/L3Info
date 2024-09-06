import matplotlib.pyplot as plt


def histo(lst_func:list)->list:
    try:
        lst_hist = [0] * len(lst_func)
        for e in lst_func:
            lst_hist[e] += 1
        """ Suppression des 0 en trop a la fin du res de hist() """
        while (not lst_hist[-1]):
            lst_hist.pop(-1)
        return lst_hist
    except:
        raise ValueError
    

def est_injective(lst_func:list)->bool:
    for e in lst_func:
        if e > 1:
            print("La fonction n'est pas injective")
            return False
    print("Cette fonction est injective")
    return True

def est_surjective(lst_func:list)->bool:
    for e in lst_func:
        if (not e):
            print("Cette fonction n'est pas surjective")
            return False
    print("Cette fonction est surjective")
    return True

def est_bijective(lst_func:list)->bool:
    return (est_injective(lst_func) and est_surjective(lst_func))


def aff_histo(lst_func:list)->None:
    MAX_VAL = max(lst_func)
    
    hist = histo(lst_func)
    max_val = MAX_VAL + 1 # iterator
    whitespace = ""
    
    print("TEST HISTOGRAMME")
    max_i = len(hist)   
    """ Affichage des valeurs """
    while max_val != 0:             # row
        for i in range(max_i):      # col
            if (hist[i] < max_val):
                whitespace = "....."
            else:
                whitespace = "...#."
            print(whitespace, end='')
        max_val -= 1
        print("")
    
    max_val = MAX_VAL
    """ Affichage du footer """
    for i in range(max_val+1):
        print("|----", end='')
    print("|")
    whitespace = ""
    for i in range(max_val+1):
        if (i < 10):
            whitespace = "  "
        elif(i < 100):
            whitespace = " "
        else:
            whitespace = ""
        print(whitespace, i, end=' ')

def aff_histo2(lst_func:list)->None:
    plt.hist(lst_func)
    plt.show()




if (__name__ == '__main__'):
    list1 = [1,2,3,4,5,6,7,8,9,0]
    list3 = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    list2 = [1,2,3,4,5,6,5,3,1,7,8,9,0]
    list4 = [0, 2, 4, 4, 6, 6, 6, 8, 8, 8, 8, 7]
    aff_histo2(list4) 
    """ if (est_bijective(histo(list1))):
        print("Cette fonction est donc bijective") """