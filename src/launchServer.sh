#!/bin/bash
# script qui lance le serveur minecraft dont le dossier est mis en argument
if [ -d $1 ]
then
	cd $1
	./../src/startServer.sh $1
	cd ..
	exit 0
else
	echo "le dossier $1 n'existe pas, le script s'utilise de cette maniere ./launchServer [dossier du serveur]"
	exit 1
fi
