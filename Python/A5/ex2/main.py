from random import *


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


if (__name__ == "__main__"):
    # Test de votre code
    lst_sorted = [0, 1, 2, 3, 4, 5, "qwertyuiop", 3.1415, True, 0x47]
    res = mix_list(lst_sorted)
    print(type(res), res)

    pass


