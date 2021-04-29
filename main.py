import os
import time
import sys
import subprocess
from src.EditOption import EditOption

def Clear():
    os.system("clear")

def CreateServer():
    Clear()
    print("=====createServer=====")
    version = input("Quelle Version du jeu voulez vous ? : ")
    versions = ["1.2.5","1.3.2","1.4.4","1.4.5","1.5.1","1.6.1","1.6.4","1.7.3","1.7.5","1.7.7","1.7.9","1.8","1.8.2","1.8.4","1.8.6","1.8.8","1.9","1.9.2","1.9.4","1.10.1","1.11","1.11.2","1.12.1","1.13","1.13.2","1.14.1","1.14.3","1.15","1.15.2","1.16.1","1.16.3","1.16.5","1.3.1","1.4.2","1.4.6","1.4.7","1.5.2","1.6.2","1.7.2","1.7.4","1.7.6","1.7.8","1.7.10","1.8.1","1.8.3","1.8.5","1.8.7","1.8.9","1.9.1","1.9.3","1.10","1.10.2","1.11.1","1.12","1.12.2","1.13.1","1.14","1.14.2","1.14.4","1.15.1","1.16","1.16.2","1.16.4"]
    if version not in versions:
        print("la version que vous avez entré n'existe pas, nous vous renvoyons au menu")
        time.sleep(2)
    else:
        print("voici la liste des serveurs que vous avez deja : ")
        folderList = FolderList()
        name = input("Quel est nom que vous voulez donner au serveur ? : ")
        if name in folderList:
            print("le serveur que vous avez entré existe deja, nous vous renvoyons au menu")
            time.sleep(2)
        else:
            print("le serveur va etre créé")
            time.sleep(1)
            subprocess.run(["sh","./src/createServer.sh",version,name])
    time.sleep(2)
    ShowMenu()

def DeleteServer():
    Clear()
    print("========DeleteServer========")
    print("voici la liste des serveurs que vous avez : ")
    folderList = FolderList()
    name = input("Quel est le nom du serveur que vous voulez supprimer ? : ")
    if name in folderList:
        response = input("Voulez vous vraiment supprimer le serveur {} ? (tapez oui pour le supprimer) : ".format(name))
        if response == "oui":
            print("le serveur va être supprimé")
            subprocess.run(["sh","./src/deleteServer.sh",name])
        else:
            print("le serveur ne sera pas supprimé")
    else:
        print("le serveur ne semble pas exister, nous vous renvoyons au menu")
    time.sleep(3)
    ShowMenu()

def LaunchServer():
    Clear()
    print("========LaunchServer========")
    print("voici la liste des serveurs que vous avez : ")
    folderList = FolderList()
    name = input("Quel est le nom du serveur que vous voulez lancer ? : ")
    if name in folderList:
        subprocess.run(["sh","./src/launchServer.sh",name])
        print("le serveur {} est en cours de lancement".format(name))
    else:
        print("le serveur ne semble pas exister, nous vous renvoyons au menu")
    time.sleep(3)
    ShowMenu()

def ModifyOptions():
    print("========EditOptions========")
    print("voici la liste des serveurs que vous avez : ")
    folderList = FolderList()
    name = input("Quel est le nom du serveur que vous voulez éditer ? : ")
    if name in folderList:
        EditOption(name)
    else:
        print("le serveur ne semble pas exister, nous vous renvoyons au menu")
    time.sleep(3)
    ShowMenu()

def Monitoring():
    Clear()
    print("Monitoring")
    ShowMenu()

def Save():
    Clear()
    print("========AutoSave========")
    print("voici la liste des serveurs que vous avez : ")
    folderList = FolderList()
    name = input("dans quel serveur voulez vous lancer la saubegarde automatique ? : ")
    if name in folderList:
        subprocess.run(["sh","./src/script_backup.sh",name])
        print("le serveur {} a été sauvegardé".format(name))
    else:
        print("le serveur ne semble pas exister, nous vous renvoyons au menu")
    time.sleep(3)
    ShowMenu()

def FolderList() :
    folderList = next(os.walk("."))[1]
    if ".git" in folderList:
        folderList.remove(".git")
    if "src" in folderList:
        folderList.remove("src")
    if "__pycache__" in folderList:
        folderList.remove("__pycache__")
    for folder in folderList:
        print("[" + folder + "]" ,end=" ")
        print("")
    return folderList

def Help():
    Clear()
    print("==========Help==========")
    print("Bienvenue dans notre page d'aide, si tu te trouves ici c'est que tu es perdu")
    print("Il te suffit de taper le numéro de ce que tu veux faire")
    print("Pour quitter le menu, il faut écrire \"stop\"")
    print("========================")
    time.sleep(5)
    ShowMenu()

def ErrorMessage():
    print("Erreur: Tu dois taper un chiffre entre 1 et 6")
    time.sleep(5)
    ShowMenu()

def Stop():
    Clear()
    print("Le programme s'est arreté")
    sys.exit(0)

def ShowMenu():
    funcChoice = {
        "1": CreateServer,
        "2": LaunchServer,
        "3": ModifyOptions,
        "4": Monitoring,
        "5": Save,
        "6": DeleteServer,
        "7": Help,
        "stop": Stop
    }
    Clear()
    print("==========MENU==========")
    print("1.Creer un serveur")
    print("2.Lancer un serveur")
    print("3.Modifier les options d'un serveur")
    print("??4.Monitoring d'un serveur??")
    print("5.Sauvegardes")
    print("6.Supprimer un serveur")
    print("7.Help")
    print("========================")
    response = input("Veuillez tapez votre choix: ")
    func = funcChoice.get(response, ErrorMessage)
    print(response)
    err = func()
    if err != None:
        print("erreur")

ShowMenu()