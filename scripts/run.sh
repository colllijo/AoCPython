#!/bin/bash

#Check that script is run from root directory
if [[ ! ( "$0" =~ (\./)?scripts/run.sh ) ]]; then
	echo "Please run this script from the base directory as \"scripts/run.sh -y year -d day -p part\"."
	exit 1
fi

flags=""

while getopts y:d:p: flag
do
    case "${flag}" in
        y) flags+=" -y ${OPTARG}";;
        d) flags+=" -d ${OPTARG}";;
        p) flags+=" -p ${OPTARG}";;
    esac
done

time python3 main.py $flags