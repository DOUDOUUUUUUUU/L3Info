from math import inf

IMC = {
    16.5 : " maigreur",
    18.5 : " corpulence normale",
    25 : "surpoids",
    30 : "obesité modéré",
    35 : "obésité morbide",
    inf: "obésité morbide"
}

def message_imc(imc:float)->str:
    imc_list = list(IMC.keys())
    message = " dénutrition ou famine"
    i = 0
    while imc > imc_list[i]:
        message = list(IMC.values())[i]
        i += 1
#    for i in range(len(imc_list)):
#        if imc >= imc_list[i]:
#            message = list(IMC.values())[i]
    return message

if (__name__ == "__main__"):
    print(message_imc(42))