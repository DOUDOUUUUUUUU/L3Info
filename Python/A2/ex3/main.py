
def separation(lst:list):
    lsep = [0] * len(lst)
    i_neg = 0
    i_pos = len(lst) - 1
    
    for i in lst:
        if (i < 0):
            lsep[i_neg] = i
            i_neg += 1
        elif (i > 0):
            lsep[i_pos] = i
            i_pos -= 1
    while (i_neg < i_pos):
        lsep[i_neg] = 0
        i_neg += 1
    return lsep


if (__name__ == "__main__"):
    print(separation([1, -2, 3, -4, 5, -6, 0]))