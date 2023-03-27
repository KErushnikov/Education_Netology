#!/bin/bash

i=0
mydir=$(pwd)

if [ -n "$1" ]
then
cd $1
for obj in $(ls)
do
        echo $obj
        let "i = i + 1"
done
echo "Total objects: $i"
cd $mydir
else
for obj in $(ls)
do
        echo $obj
        let "i = i + 1"
done
echo "Total objects: $i"
fi