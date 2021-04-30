# Projet Infra & SI - Serveur Minecraft

Réalisation d'un gestionnaire d'un serveur du jeu Minecraft . 

---

##  Ressources nécessaires

* Tout d’abord il est recommandé d’opter pour une distribution Debian (distribution que nous avons utilisé pour la réalisation du projet) 

* Les scripts nécessaires pour le projet se situent sur notre git, il faudra donc installer git sur la machine si celui-ci n’est pas déjà présent : ``` apt install git ``` .  

* Il faudra également installer java sur la machine pour pouvoir exécuter le serveur : ``` apt install default-jre ``` .

* Pour télécharger la version du serveur , il faudra installer le package wget : ``` apt install wget ```

* Pour pouvoir superviser l’activité du serveur, il faudra installer netdata. Pour cela on exécute  le script présent dans la documentation officiel de l’installation de netdata : ``` bash <(curl -Ss https://my-netdata.io/kickstart.sh) ``` .

* Par ailleurs, il nous faut le package curl pour pouvoir exécuter le script précédent : ``` apt install curl ``` .

* Il est recommandé de regarder sur sa machine si python3 est installé. Si ce n’est pas le cas, installez-le : ``` apt install python3 ``` .

* Pour finir, pour pouvoir exécuter le serveur minecraft sur un autre terminal, il faudra installer le package screen : ``` apt install screen ```

---
## Création du programme

### **Menu du serveur**

* Pour accéder au menu, il suffit d’exécuter le programme main.py avec python 3 : ``` python3 main.py ``` 

* Depuis ce menu, nous avons plusieurs options à notre disposition :
    *  Créer un serveur
    *  Lancer le serveur
    *  Modifier les options d'un serveur 
    *  Sauvegarde 
    *  Aide

### **Création et lancement d'un serveur** 

* Depuis le menu, on choisit l’option 1 « Créer un serveur ». 
* Ensuite on choisit la version du jeu (toutes les versions qui disposent d’un serveur officiel en ce moment sont disponibles) et le nom du serveur.

* On peut retrouver les serveurs que vous allez créer dans le dossier où se situe le ``` main.py ```

* On retourne sur le menu ``` main.py ``` pour lancer le serveur, on indique le nom du serveur que l’on a crée précédemment, et le serveur se lance.

* Par défaut c’est le port 25565 qui sera utilisée pour le serveur, il faut obligatoirement configurer le port forwarding de votre box pour que des ordinateurs appartenant à un autre réseau d’accéder au serveur.

### **Options d'un serveur**  

* Depuis le menu, on choisit l’option 3 « Modifier les options d'un serveur ». 

* Tout d'abord on choisit le dossier du serveur que l'on à crée.

*  Lorsque les options sont affichées, on choisit les options que l'on veut modifier et on indique les changements.

### **Sauvegarde automatique** 

* Depuis le menu, on choisit l’option 4 « Sauvegarde ». 

* Pour sauvegarder le serveur , on copie le dossier ```world ``` présent dans le dossier du serveur dans le dossier ``` saves ```. 



### **Monitoring** 

* Pour la partie monitoring, il suffit de lancer netdata depuis sa machine :  ``` systemctl start netdata ``` 
* On vérifie si il est bien lancé : ``` systemctl status netdata ```
On ouvre le fichier de configuration de netdata avec un éditeur : ``` vim /etc/netdata/netdata.conf ``` 
* Recherchez la section ``` [web] ```, décommentez les lignes suivantes :
     ```
    [web]
 	
        web files owner = netdata
   	    web files group = netdata  

    ```
* Sauvegarder les modifications puis redémarrer netdata : ``` systemctl restart netdata ```

* Depuis un navigateur sur Windows rechercher dans la barre : http://(ip de la machine):19999 

* Netdata fournit diverses infos de votre machine Linux  

* Pour personnaliser le tableau de bord de netdata , il faut créer un compte netdata puis se rendre dans la catégorie " war room ", puis selectionner la war romm et cliquer sur le bouton " Add " à droite 

* Copier le script qui s'affiche à droite , éxécuter le depuis la machine linux 

* cliquer sur l'onglet " Dashboard " et créer un nouveau tableau de bord

* Ajouter les noeuds souhaités sur le tableau de bord 
