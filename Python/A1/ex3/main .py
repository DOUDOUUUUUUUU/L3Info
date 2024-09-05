from math import sqrt

def discriminant(a:float,b:float,c:float)->float:
    return b*b - (4 * a * c)

def racine_unique(a:float,b:float)->float:
    return (-b) / (2*a)

def racine_double(a:float,b:float,delta:float,num:float)->float:
    if num == 1:
        return ((-b) + sqrt(delta)) / (2*a)
    else:
        return ((-b) - sqrt(delta)) / (2*a)

def str_equation(a:float,b:float,c:float)->str:
    equation = ""
    if a:
        equation += str(a) + "x^2 "
    if b > 0:
        equation += " + "+ str(b) +"x"
    elif b < 0:
        equation += str(b) +"x"
    if c > 0:
        equation += " + "+ str(c)
    elif c < 0:
        equation += str(c)
    return equation + " = 0 "

def solution_equation(a:float,b:float,c:float)->str:
    message = "solution de l'équation :"+ str_equation(a,b,c)
    delta = discriminant(a,b,c)
    if delta == 0:
        message += "solution unique : x ="+ str(racine_unique(a,b))
    elif delta > 0:
        message += "deux racines distinctes :\nx1 = "+ str(racine_double(a,b,delta,1))
        message += "x2 = "+ str(racine_double(a,b,delta,2))
    else:
        message += "Pas de racine réelles"
    return message
        
def equation(a:float,b:float,c:float)->None:
    print("solution de l'équation :",str_equation(a,b,c))
    delta = discriminant(a,b,c)
    if delta == 0:
        print("solution unique : x =", racine_unique(a,b))
    elif delta > 0:
        print("deux racines distinctes :\nx1 = ",racine_double(a,b,delta,1))
        print("x2 = ",racine_double(a,b,delta,2))
    else:
        print("Pas de racine réelles")

def equation_bis(a,b,c):
    print(solution_equation(a,b,c),"\n")

def test():
    equation_bis(4,7.3,8.9)
    equation_bis(9,850,8.9)
    equation_bis(4,3,1)
    equation_bis(4,4,1)
    equation_bis(-7,1,-3)
    
test()