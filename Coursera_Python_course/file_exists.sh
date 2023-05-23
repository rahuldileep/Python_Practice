#!/bin/bash

cat list.txt | while read LINE; do
    echo $LINE
done

files=$(grep " jane " list.txt | cut -d" " -f 3)

for i in $files; do
  if test -e $i; then echo "file exists";
  else echo "file doesn't exist"; fi 
done
