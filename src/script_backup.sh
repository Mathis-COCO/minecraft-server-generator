#!/bin/bash

if [ $# -eq 1 ]
then
	while screen -ls $1 
	do
		DATE=$(date +%d-%m-%Y-%H-%M-%S) 
		screen -rd $1 -X -p0 eval "stuff 'save-all'^m"
		if [ ! -d saves ]
		then
			mkdir saves
		fi
		cd saves
		mkdir $1$DATE
		cd ..
		cp -r $1/world/ saves/$1$DATE
		sleep 600
	done
else
	echo "Problème de paramètres : ./script_backup.sh <nom du serveur>"
fi
