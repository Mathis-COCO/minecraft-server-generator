#!/bin/bash

if [ $# -eq 2 ]
	then
	cp -r $1 $2
	else
	echo "Problème de paramètres : ./recup_backup.sh <chemin de la sauvegarde 'world'> <chemin du dossier du serveur"
fi
