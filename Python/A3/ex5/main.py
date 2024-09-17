#40 91 123

def ouvrante(char:str)->bool:
    try:
        assert len(char) == 1
    except:
        raise ValueError
    return char in ['(', '[', '\{']

def fermante(char:str)->bool:
    try:
        assert len(char) == 1
    except:
        raise ValueError
    return char in [')', ']', '\}']


def reverse(char:str):
    try:
        assert len(char) == 1
    except:
        raise ValueError
    
    lst_open = ['(', '[', '\{']
    lst_close = [')', ']', '}']
    
    if (ouvrante(char)):
        for i, e in enumerate(lst_open):
            if (char == e):
                return lst_close[i]
    elif (fermante(char)):
        for i, e in enumerate(lst_close):
            if (char == e):
                return lst_open[i]
    else:
        return char
            
def operateur(char:str)->bool:
    try:
        assert len(char) == 1
    except:
        raise ValueError
    return char in ['+', '-', '*', '/']

def nombre(string:str)->bool:
    for e in string:
        if (not e.isdigit()):
            return False
    return True

def valid_character(char:str)->bool:
    try:
        assert len(char) == 1
    except:
        raise ValueError
    return True if (nombre(char and operateur(char) and ouvrante(char) and fermante(char))) else False

def verif_parenthese(exp:str)->bool:
    lst_exp = list(exp)
    cache = []
    for e in lst_exp:
        if (fermante(e)):
            try:
                if (len(cache) == -1):
                    return False
                elif (cache[-1] != reverse(e)):
                    return False
                cache.pop()
            except:
                return False
        elif (ouvrante(e)):
            cache.append(e)
    return True if len(cache) == 0 else False

if (__name__ == "__main__"):
    
    print(verif_parenthese("(3+2)*6-1"))
    
    pass