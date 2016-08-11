#!/usr/bin/env/python
# -*- coding:Utf-8 -*-

"""

LucieTimeLib .. > Main.py

Librairie des éléments temporels du robot "Lucie". Permet de connaitre l'heure et d'effectuer des opérations avec.


=== STICKYNOTES =====================

#toDo :

[OK] Récupérer l'heure sur le réseau
[+] Mettre l'heure du système à jour
[+] gérer les heures d'hiver / heures d'été


"""

import datetime
import ConfigParser
import urllib2


mois  = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]


# Classes

class Config():
    """
    Juste une classe pour stocker les variables de config...
    """
    def __init__(self):
        pass
    
    def load(self, file):
        """
        Charger la config depuis un fichier config
        """
        configParser = ConfigParser.RawConfigParser()   
        configParser.read(file)
        self.gmtdiff = configParser.get('jetlag', 'gmtdiff')
    

class Timer():
    """
    TIMER
    
    Classe d'un objet Chronomètre.
    
    Exemple :
    
    monChrono = Timer()
    monChrono.start()
    ...
    monChrono.time() -> temps en secondes depuis start() (int)
    """
    def __init__(self):
        pass
    
    def start(self):
        # Relever le temps dans une variable d'heure initiale
        self.startTime = datetime.datetime.now()
    
    def read(self):
        return datetime.datetime.now() - self.startTime


# Définitions

def __init__():
    global mois,jours
    # Creer les listes globales
    mois  = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

def get_date_time():
    return str(datetime.datetime.now())

def time_natural_language():
    a = ((get_date_time().split(" ")[1]).split(".")[0]).split(":")
    #print "il est "+str(a[0])+" heures, "+str(a[1])+" minutes et "+str(a[2])+" secondes."
    return "il est "+str(a[0])+" heures, "+str(a[1])+" minutes et "+str(a[2])+" secondes." # On se moque de l'orthographe! c'est phonétique

def time_natural_language_short():
    a = ((get_date_time().split(" ")[1]).split(".")[0]).split(":")
    #print "il est "+str(a[0])+" heures, "+str(a[1])+" minutes et "+str(a[2])+" secondes."
    return "il est "+str(a[0])+" heures "+str(a[1])+"."


def date_natural_language():
    global mois,jours
    a = (get_date_time().split(" ")[0]).split("-")
    #print("Nous sommes le "+str(a[2])+" "+str(mois[int(a[1])-1])+" "+str(a[0])+". Et je m'excuse, mais je ne sais pas déterminer quel jour de la semaine nous sommes. C'est ça de faire tourner un logiciel béta!")
    return "Nous sommes le " + jours[datetime.datetime.today().weekday()] + " " + str(a[2])+" "+str(mois[int(a[1])-1])+" "+str(a[0])+"."

def date_and_time_natural_language():
    return date_natural_language() + " et " + time_natural_language_short()


def day_natural_language():
    return "Nous sommes " + jours[datetime.datetime.today().weekday()]

def get_from_network():
    """
    http://just-the-time.appspot.com renvoie une string sous la forme : 2016-05-31 12:45:05
    Attention, l'heure renvoyée est calée sur GMT !
    """
    response = urllib2.urlopen('http://just-the-time.appspot.com')
    string = response.read()
    string = string.split(" ") # Là ça donne une liste : [date,time]
    time = string[1].split(":")
    h=time[0]
    m=time[1]
    s=time[2]
    
    
    d = 0
    mo = 0
    y = 0
    return [d,mo,y,h,m,s]

def test_lib():
    """
    Tester la librairie.
    Personnaliser la fonction pour tester des éléments en particuliers.
    """
    
    print "création d'un chrono & démarrage\n\n"
    monChrono = Timer()
    monChrono.start()
    
    print "time_natural_language()"
    print time_natural_language()
    
    print("\n")
    
    print "date_and_time_natural_language()"
    print date_and_time_natural_language()
    
    print("\n")
    
    print "time_natural_language_short()"
    print time_natural_language_short()
    
    print("\n")
    
    print "date_natural_language()"
    print date_natural_language()
    
    print("\n")
    
    print "day_natural_language()"
    print day_natural_language()

    print "\n\nlecture chrono : "
    print(monChrono.read())
    
    print("\n")

    print("chargement config depuis le fichier 'config'...")
    config = Config()
    config.load("config")
    print("on est à GMT+" + str(config.gmtdiff))
    
    print("\n")

    print("Lecture de l'heure sur le réseau...")
    get_from_network()
    print("L'heure récupéré sur le réseau est " + str(config.gmtdiff))


###  T E S T  ###

# Commenter pour désactiver le mode test

test_lib()
