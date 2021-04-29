#!/bin/bash
# Supression au choix d'un serveur minecraft en choisisssant le dossier du serveur à supprimer en premier paramètre

if [ $# -eq 1 ]
then
	if [ -d $1 ]
	then	
	rm -rf $1
	echo -e " Le serveur $1 à été bien supprimé "
	else	
	echo -e "le serveur $d1 n'existe pas "
	fi
else
	echo "le script n'a pas le bon nombre de paramètres"
	echo " il s'utilise de la manière suivante: ./deleteServer.sh [nom du serveur à delete]"
fi
			
	
