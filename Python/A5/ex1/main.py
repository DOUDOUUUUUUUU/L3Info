from random import *

def gen_list_random_int(nb:int=10, min:int=0, max:int=10)->list:
    if (min >= max):
        raise ValueError
    return [randint(min, max-1) for i in range(nb)]



if (__name__ == "__main__"):
    print(gen_list_random_int())
    pass