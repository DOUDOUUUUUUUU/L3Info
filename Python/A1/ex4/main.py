import datetime as d

def date_est_valide(jour:int, mois:int, annee:int)->bool:
    try:
        if (d.date(annee, mois, jour)):
            return True
    except:
        return False

def saisie_date_naissance()->d.datetime:
    saisie_flag = 1
    while saisie_flag:
        print("Saisissez votre jour de naissance")
        jour = int(input())
        print("Saisissez votre mois de naissance")
        mois = int(input())
        print("Saisissez votre annee de naissance")
        annee = int(input())
        if not (date_est_valide(jour, mois, annee)):
            print("Erreur de saisie\n")
        else:
            saisie_flag = 0
    return d.datetime(annee, mois, jour).date()

def age(date_naissance:d.datetime)->int:
    today = int(d.datetime.today().date().strftime("%Y"))
    naissance = int(date_naissance.strftime("%Y"))
    return today - naissance

def est_majeur(date_naissance:d.date)->bool:
    today = int(d.datetime.today().date().strftime("%Y"))
    naissance = int(date_naissance.strftime("%Y"))
    return (today - naissance) > 18

def test_acces():
    naissance = saisie_date_naissance()
    aage = age(naissance)
    if (est_majeur(naissance)):
        print("Bonjour, vous avez ",aage,"ans, Acces autorise")
    else:
        print("Desole, vous avez ",aage,"ans, acces interdit")





test_acces()