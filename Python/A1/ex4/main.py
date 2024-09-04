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
    return d.datetime(annee, mois, jour, 0, 0, 0, 0)

def age(date_naissance:d.datetime)->int:
    today = d.datetime.now().date()
    age = today - date_naissance
    return age//365








print(age(d.date(2012, 12, 12)))