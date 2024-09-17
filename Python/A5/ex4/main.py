from random import *

def extract_elements_list(lst:list, n:int)->list:
    new_list = []
    cache = []
    i = 0
    
    if (not lst or n > len(lst)):
        raise ValueError
    
    while i != n:
        rdm = randint(0, len(lst) - 1)
        if (rdm not in cache):
            cache.append(rdm)
            new_list.append(lst[rdm])
            i += 1
    
    return new_list


if (__name__ == "__main__"):
    print(extract_elements_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0))
    pass