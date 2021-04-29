#!/bin/bash

# Supression au choix d'un serveur minecraft en choisisssant le dossier du serveur à supprimer

echo -e " Quel dossier voulez-vous supprimer? "

dir=""

read dir

# si le dossier existe

if [ -d $dir ]	

then	
	
	rm -r $dir
	
	echo -e " Le dossier $dir à été bien supprimé "
		
else
		
	echo -e "le dossier $dir n'existe pas "
		
fi
			
	
