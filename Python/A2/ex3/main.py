
def separation(lst:list):
    lsep = []
    i_neg = 0
    i_pos = len(lst) - 1
    
    for i in lst:
        if (i < 0):
            lsep[i_neg] = i
            i += 1
        elif (i > 0):
            lsep[i_pos] = i
            i_pos -= 1
    while (i_neg < i_pos):
        lsep[i_neg] = 0
        i_neg += 1
    return lsep