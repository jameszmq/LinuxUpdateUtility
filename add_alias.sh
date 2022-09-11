#!/bin/bash

path=$(pwd)
filepath="${path}/upgrade_utility.py"

if [ "$#" -ne 1 ]; then
	printf "Illegal number of parameters, should be 1.\n"
	exit -1
fi

if ! alias $1 2>/dev/null ; then
	if [ -f ~/.bash_aliases ]; then
		printf "\nalias $1=\"python3 ${filepath}\"" >> ~/.bash_aliases
	else
		printf "\nalias $1=\"python3 ${filepath}\"" >> ~/.bashrc
	fi
else
	printf "Alias \"$1\" already exists. Please try using another alias.\n"
fi

source ~/.bashrc