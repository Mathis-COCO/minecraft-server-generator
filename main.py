import os
import time
import sys
import subprocess

def Clear():
    os.system("clear")

def CreateServer():
    Clear()
    print("=====createServer=====")
    version = input("Quelle Version du jeu voulez vous ? : ")
    versions = ["1.2.5","1.3.2","1.4.4","1.4.5","1.5.1","1.6.1","1.6.4","1.7.3","1.7.5","1.7.7","1.7.9","1.8","1.8.2","1.8.4","1.8.6","1.8.8","1.9","1.9.2","1.9.4","1.10.1","1.11","1.11.2","1.12.1","1.13","1.13.2","1.14.1","1.14.3","1.15","1.15.2","1.16.1","1.16.3","1.16.5","1.3.1","1.4.2","1.4.6","1.4.7","1.5.2","1.6.2","1.7.2","1.7.4","1.7.6","1.7.8","1.7.10","1.8.1","1.8.3","1.8.5","1.8.7","1.8.9","1.9.1","1.9.3","1.10","1.10.2","1.11.1","1.12","1.12.2","1.13.1","1.14","1.14.2","1.14.4","1.15.1","1.16","1.16.2","1.16.4"]
    if version not in versions:
        return 1
    name = input("Quel est nom que vous voulez donner au serveur ? : ")
    print("Si le serveur n'existe pas deja il va etre créé")
    subprocess.run(["sh","./createServer.sh",version,name])
    ShowMenu()

    
def LaunchServer():
    Clear()
    print("========LaunchServer========")
    name = input("Quel est le nom du serveur que vous voulez lancer ?")
    subprocess.run(["sh","./launchServer.sh",name])
    print("le serveur {} est en cours de lancement".format(name))
    ShowMenu()

def ModifyOptions():
    Clear()
    print("modifyOptions")
    ShowMenu()

def Monitoring():
    Clear()
    print("Monitoring")
    ShowMenu()

def Save():
    Clear()
    print("save")
    ShowMenu()

def Help():
    Clear()
    print("help")
    ShowMenu()

def ErrorMessage():
    print("Erreur: Tu dois taper un chiffre entre 1 et 6")
    time.sleep(5)
    ShowMenu()

def Stop():
    Clear()
    print("Le programme va s'arreter")
    sys.exit(0)

def ShowMenu():
    funcChoice = {
        "1": CreateServer,
        "2": LaunchServer,
        "3": ModifyOptions,
        "4": Monitoring,
        "5": Save,
        "6": Help,
        "stop": Stop
    }
    Clear()
    print("==========MENU==========")
    print("1.Creer un serveur")
    print("2.Lancer un serveur")
    print("3.Modifier les options d'un serveur")
    print("??4.Monitoring d'un serveur??")
    print("??5.Sauvegarde??")
    print("6.Help")
    print("========================")
    response = input("Veuillez tapez votre choix: ")
    func = funcChoice.get(response, ErrorMessage)
    print(response)
    err = func()
    if err != None:
        print("erreur")






def Test():
    os.system("clear")
    print("==========MENU==========")
    print("Test")
    print("========================")

ShowMenu()