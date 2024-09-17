from random import *
from time import *
import matplotlib.pyplot as plt
import sys

def gen_list_random_int(nb:int=10, min:int=0, max:int=10):
    if (min >= max):
        raise ValueError
    return [randint(min, max-1) for i in range(nb)]

def tri(lst1:list, lst2:list)->list:
    if (not lst1):
        return lst2
    if (not lst2):
        return lst1
    if (lst1[0] <= lst2[0]):
        return [lst1[0]] + tri(lst1[1:], lst2)
    else:
        return [lst2[0]] + tri(lst1, lst2[1:])

def sort_list(lst:list)->list:
    MAX = len(lst)
    if (MAX <= 1):
        return lst
    return tri(sort_list(lst[:MAX//2]), sort_list(lst[MAX//2:]))


def perf_mix(func1:callable, func2:callable, lst_len:list, n:int)->tuple[list, list]:
    t_start, t_end = 0, 0
    moy1, moy2 = 0, 0
    t1, t2 = [], []
    
    
    for i in range(len(lst_len)):
        rdm_list = gen_list_random_int(lst_len[i], 0, 1000000)
        for j in range(n):
            t_start = perf_counter()
            func1(rdm_list)
            t_end = perf_counter()
            moy1 += (t_end - t_start)
            
            t_start = perf_counter()
            func2(rdm_list)
            t_end = perf_counter()
            moy2 += (t_end - t_start)
        moy1 /= n
        moy2 /= n
        t1.append(moy1)
        t2.append(moy2)
    
    return (t1, t2)



def graph(moy:tuple[list, list], spl:list)->None:
    """ moy_1 = moy[0]
    moy_2 = moy[1] """
    
    
    
    fig, ax = plt.subplots() 
    #Dessin des courbes, le premier paramètre  
    #correspond aux point d'abscisse le 
    #deuxième correspond aux points d'ordonnées 
    #le troisième paramètre, optionnel permet de  
    #choisir éventuellement la couleur et le marqueur 
    ax.plot(spl,moy, 'bo-',label='sort_list') 
    #ax.plot(spl,moy_2,  'r*-', label='Native sorted()') 
    ax.set(xlabel='Nombre d\'Élément dans la liste', ylabel='Temps', 
        title='Complexité mix et shuffle') 
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 
    #fig.savefig("test_extr_sample.png") 
    plt.show() 
    pass



if (__name__ == "__main__"):

    sys.setrecursionlimit(1500)
    lst_len = [i for i in range(50, 100)]
    moy = perf_mix(sort_list, sorted, lst_len, 100)
    print(moy)
    graph(moy[1], lst_len)
    sys.setrecursionlimit(1000)
    sorted()
    pass