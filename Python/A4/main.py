import numpy as np

def my_searchsorted(lst:list, num:int)->int:
    i = 0
    while num < lst[i]:
        i += 1
    return i

def my_where(lst:list, num:int)->list:
    res_lst = []
    len_f = len(lst[0])
    max = len(lst) * len_f
    if (len(lst[0]) != 1):
        
    for i in range(max):
        if (lst[i] == num):
            res_lst.append(i)
    return