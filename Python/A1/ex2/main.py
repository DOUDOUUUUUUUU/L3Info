
def annee_bisextile(annee:int)->bool:
    bis = False
    if (annee % 4 == 0):
        if (annee % 100 != 0):
            bis = True
        elif (annee % 400 == 0):
            bis = True
    return bis



def test():
    print("1", annee_bisextile(1984))
    print("2", annee_bisextile(1986))
    print("3", annee_bisextile(2003))
    print("4", annee_bisextile(2000))
    print("5", annee_bisextile(1900))
    print("6", annee_bisextile(1904))
    print("7", annee_bisextile(1000))
    

    
    





if (__name__ == "__main__"):
    test()
    