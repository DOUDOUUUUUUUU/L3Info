from time import *
from random import *
import matplotlib.pyplot as plt

def gen_list_random_int(nb:int=10, min:int=0, max:int=10):
    if (min >= max):
        raise ValueError
    return [randint(min, max-1) for i in range(nb)]

def mix_list(lst_to_mix:list)->list:
    if (not lst_to_mix):
        raise ValueError
    new_lst = []
    cache = []
    while len(cache) != len(lst_to_mix):
        index = randint(0, len(lst_to_mix) - 1)
        if (index not in cache):
            new_lst.append(lst_to_mix[index])
            cache.append(index)
    if (new_lst == lst_to_mix):
        return mix_list(lst_to_mix)
    return new_lst

def extract_elements_list(lst:list, n:int)->list:
    new_list = []
    cache = []
    i = 0
    if (not lst or n > len(lst)):
        raise ValueError
    max = len(lst) - 1
    while i != n:
        rdm = randrange(0, max)
        if (rdm not in cache):
            cache += [rdm]
            new_list.append(lst[rdm])
            i += 1
    
    return new_list

def perf_mix(func1:callable, func2:callable, lst_len:list, n:int)->tuple[list, list]:
    t_start, t_end = 0, 0
    moy1, moy2 = 0, 0
    t1, t2 = [], []
    
    
    for i in range(len(lst_len)):
        rdm_list = gen_list_random_int(lst_len[i], 0, 1000000)
        for j in range(n):
            t_start = perf_counter()
            func1(rdm_list, 10)
            t_end = perf_counter()
            moy1 += (t_end - t_start)
            
            t_start = perf_counter()
            func2(rdm_list, 10)
            t_end = perf_counter()
            moy2 += (t_end - t_start)
        moy1 /= n
        moy2 /= n
        t1.append(moy1)
        t2.append(moy2)
    
    return (t1, t2)


def graph(moy:tuple[list, list], spl:list)->None:
    moy_1 = moy[0]
    moy_2 = moy[1]
    
    
    
    fig, ax = plt.subplots() 
    #Dessin des courbes, le premier paramètre  
    #correspond aux point d'abscisse le 
    #deuxième correspond aux points d'ordonnées 
    #le troisième paramètre, optionnel permet de  
    #choisir éventuellement la couleur et le marqueur 
    ax.plot(spl,moy_1, 'bo-',label='extract_element_list') 
    ax.plot(spl,moy_2,  'r*-', label='random.sample') 
    ax.set(xlabel='Nombre d\'Élément dans la liste', ylabel='Temps', 
        title='Complexité mix et shuffle') 
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 
    #fig.savefig("test_extr_sample.png") 
    plt.show() 
    pass



if (__name__ == "__main__"):
    elt1 = [10, 100, 1000, 10000]
    elt2 = [100, 1000, 10000, 100000]
    moy_mix_shuffle = ([2.7567929999999986e-05, 0.0005169306992999997, 0.026502805166992983, 3.13542886683167],
                       [3.5554200000000902e-06, 2.3577214199999875e-05, 0.00021554364214200692, 0.0022562762464219616])
    moy_extr_sample = ([0.0004417470129999994, 0.00010054657101300025, 0.00014490109557101417, 0.00010790349209556764],
                       [2.4890227000000154e-05, 2.565672222699808e-05, 3.4545877722225964e-05, 3.41478198777232e-05])
    #print(perf_mix(extract_elements_list, sample, [100, 1000, 10000, 100000], 1000))
    moy = perf_mix(extract_elements_list, sample, elt2, 100000)
    print(moy)
    graph(moy, elt2)
    
    pass

