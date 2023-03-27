#!/bin/bash

method=$1
message=$2

if [ $# != 2 ]
then
echo "Wrong number of parameters for this script"
exit
else
    if [[ -n "$1" && -n "$2" && "$method" == "crypt" ]]
    then
    crypted=`echo -n $message | base64`
    echo "Encrypting..."
    echo "$crypted"
        elif [[ -n "$1" && -n "$2" && "$method" == "decrypt" ]]
        then
        decrypted=`echo $message | base64 --decode`
        echo "Decrypting..."
        echo "$decrypted"
    else
    echo "Input correct method"
    fi
fi