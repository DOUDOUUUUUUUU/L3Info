TYPE_LETTRE = {
    "lettre verte": 1,
    "ecopli": 2,
    "prioritaire": 3,
}

TARIF_LETTRE_VERTE = {
    "20": 1.16,
    "100": 2.32,
    "250": 4,
    "500": 6,
    "1000": 7.50,
    "3000": 10.50
}
TARIF_COMPLEMENT_LETTRE_VERTE_PRIO = {
    "om1": 5,
    "om2": 11
}
TARIF_LETTRE_ECOPLI = {
    "20": 1.14,
    "100": 2.28,
    "250": 3.92
}
TARIF_COMPLEMENT_ECOPLI = {
    "om1": 2,
    "om2": 5
}

TARIF_LETTRE_PRIO = {
    "20": 1.16,
    "100": 2.86,
    "250": 5.26,
    "500": 7.89,
    "3000": 11.44,
}


#########################################################


def get_net_price(info_lettre:list)->float:
    '''fonction qui calcule le prix net de la lettre (juste par rapport au poids)'''
    prix_net = 0
    liste_clefs = []
    tarif_lettre= {}
    
    if info_lettre[0] == 1:
        liste_clefs = list(TARIF_LETTRE_VERTE.keys())
        tarif_lettre= TARIF_LETTRE_VERTE
    elif info_lettre[0] == 2:
        liste_clefs = list(TARIF_LETTRE_ECOPLI.keys())
        tarif_lettre= TARIF_LETTRE_ECOPLI
    elif info_lettre[0] == 3:
        liste_clefs = list(TARIF_LETTRE_PRIO.keys())
        tarif_lettre= TARIF_LETTRE_PRIO
    
    for i in range(0, len(liste_clefs) - 1):
        if (float(liste_clefs[i]) < info_lettre[1]):
            prix_net = tarif_lettre.get(liste_clefs[i+1])
        
    return prix_net


def get_complement(info_lettre:list)->float:
    '''fonction calculant les couts additionnels'''
    cout_additionnel = 0
    
    if (not info_lettre[2]):
        return 0
    
    poids = info_lettre[1]
    while poids > 0:
        cout_additionnel += info_lettre[2] / 100
        poids -= 10
    return cout_additionnel


def get_info_letter(info_lettre:list)->list:
    '''fonction qui renvoie les caracteristiques de la lettre a partir des infos fournies'''
    type_lettre_flag = 1
    poids_lettre_flag = 1
    om_flag = 1
    tarif_om = {}

    while type_lettre_flag:         ## demande du type de lettre
        print("Quel type de lettre voulez-vous envoyer ? (lettre verte, ecopli, prioritaire)")
        type_lettre = str(input())
        if (type_lettre in TYPE_LETTRE.keys()):
            info_lettre.append(TYPE_LETTRE.get(type_lettre))
            type_lettre_flag = 0
        else:
            print("Veuillez selectioner un type de lettre\n")

    while poids_lettre_flag:        ## demande du poids de la lettre
        print("Veuillez indiquer le poids de la lettre (en grammes)")
        poids_lettre = input()
        if (poids_lettre > 0):
            info_lettre.append(poids_lettre)
            poids_lettre_flag = 0
        else:
            print("Veuillez inserer un poids valide")

    ## demande si la lettre va aller outre mer ou pas
    print("Veuillez indiquer ou envoyer la lettre (om1, om2, autre)")           
    om = str(input())
    if (info_lettre[0] % 2 == 1): #selection des tarifs lettre verte\prioritaire car sont les memes 
        tarif_om = TARIF_COMPLEMENT_LETTRE_VERTE_PRIO
    else:
        tarif_om = TARIF_COMPLEMENT_ECOPLI
        
    if (om in tarif_om.keys()):
        info_lettre.append(tarif_om.get(om))
    else:
        info_lettre.append(0)

    return info_lettre


def main()->int:
    '''fonction principale'''
    prix = 0
    info = []
    
    info = get_info_letter(info)    
    prix = get_net_price(info) + get_complement(info)
    return prix



if (__name__ == '__main__'):
    print(main())