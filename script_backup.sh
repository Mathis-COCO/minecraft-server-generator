#!/bin/bash

nom=""

while screen -ls $nom 
do
	screen -rd $nom -X -p0 eval "stuff 'save-all'^m"
	if [ $# -eq 2 ]
	then
		if [ -d $2 ] 
			then
			cp -r $1 $2
			sleep 30
			else
			mkdir $2
			cp -r $1 $2
			sleep 30
		fi
	else
	echo "Problème de paramètres : ./script_backup.sh <chemin du dossier 'world' chemin pour la sauvegarde du dossier 'world'"
	fi
done
