#!/bin/bash
# A simple script to sync all git subdir 

for d in `ls`; do 
	repo="$d/.git"
	if [ -d $repo ]; then
	  echo "Sycning $d";
	  cd ${d}; git pull origin master; git push origin master; cd ..;
	  echo "-----------------------------------";
	fi;
done
