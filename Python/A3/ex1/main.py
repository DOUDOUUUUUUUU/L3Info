
def full_name(arg:str)->str:
    try:
        new_arg = ""
        i = 0
        while arg[i] != " ":
            new_arg += arg[i].upper()
            i += 1
        new_arg += arg[i:]
        return new_arg
    except:
        raise NameError


def is_mail(arg:str)->tuple[int, int]:              #TODO
    i = 0
    if ('@' not in arg):
        return (0, 2)
    elif ('@' or '.' == arg[0]):
        return (0, 1)
    elif ('corse.' not in arg):
        return (0, 4)
    elif ('@univ-corse' not in arg):
        return (0, 3)
    return (1, 0)




if (__name__ == "__main__"):
    #print(full_name("qwerty"))
    #print(is_mail("test@univ-corse.fr"))
    
    pass