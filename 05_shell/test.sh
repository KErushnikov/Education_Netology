#!/bin/bash

param=$1
if [ -d $param ]
then
echo "$param - dir"
    elif [ -f $param ]
    then
    echo "$param - file"
else
echo "$param - not exist"
fi