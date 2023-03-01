#!/bin/sh

docker() {
	if [ "$1" == "build" ]; then
		docker-compose build
	elif [ "$1" == "run" ]; then
		docker-compose up
	elif  [ "$1" == "clean" ]; then
		docker-compose down
	else
		echo "Les commandes valides sont :"
		echo "- build"
		echo "- run"
		echo "- clean"
		exit 1
	fi
}

django() {
	echo "NotImplemented"
	exit 1
}

nb_args=$#

if [ $nb_args -eq 2 ]; then
	if [ "$1" == "docker" ]; then
		docker $2
	elif [ "$1" == "django" ]; then
		django $2
	fi
else
	echo "Nombre d'arguments invalide. Voir le wiki"
fi



