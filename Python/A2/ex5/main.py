
def histo(lst_func:list)->list:
    try:
        lst_hist = [0] * len(lst_func)
        for e in lst_func:
            lst_hist[e] += 1
        return lst_hist
    except:
        raise ValueError
    
def nbEmplacement(lst:list)->tuple:
    NB_VIT = 2
    nb_element = histo(lst)
    max_element = max(nb_element)
    vit = [[] * NB_VIT]
    
    if (max_element > NB_VIT):
        return vit
    print(len(nb_element))
    print(len(lst))
    for i in range(NB_VIT):
        for j, e in enumerate(nb_element):
            
            if (e):
                vit[i].append(lst[j])
                e -= 1
        
    return tuple(vit)


if (__name__ == "__main__"):
    list1 = [1, 2, 3, 4, 5, 6, 6, 2]
    print(nbEmplacement(list1))
    pass