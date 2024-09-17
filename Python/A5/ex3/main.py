from random import *

def rand_e_list(lst:list):
    try:
        return lst[randint(0, len(lst) - 1)]
    except:
        raise ValueError

if (__name__ == "__main__"):
    # Test de votre code
    lst_sorted = [0, 1, 2, 3, 4, 5, "qwertyuiop", 3.1415, True, 0x47]
    res = rand_e_list(lst_sorted)
    print(type(res), res)