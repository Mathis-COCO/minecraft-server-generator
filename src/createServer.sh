#!/bin/bash
# script creant un serveur minecraft de la version donnée en premier argument dans le repertoire donné en deuxième argument
if [ $# -eq 2 ]
then
	if [ -d $2 ]
	then
		echo "le dossier $2 existe deja, etes vous sur de vouloir creer le serveur dedans (tapez oui pour valider) :"
		rep =""
		read  rep
		if [ $rep = "oui" ]
		then
			echo "le serveur va bien etre cree dans le dossier $2"
		else
			echo "le serveur n'a pas ete cree, un dossier $2 existe deja"
			exit 1
		fi
	else
		mkdir $2
	fi
	python3 ./src/getServerVersion.py $1
	cd $2
	./../src/version.sh
	./../src/startServerFirstTime.sh
	cd ..
	python3 ./src/acceptCLUF.py $2
	exit 0
else
	echo "Il n'y a pas le bon nombre de parametres"
	echo "le script s'utilise de cette façon : ./createServer [version du serveur] [nom du dossier du serveur]"
	exit 2
fi
