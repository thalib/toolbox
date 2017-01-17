#!/bin/bash
# A simple script to sync all git subdir 

repo_sync() {
	echo "Start sync ${d}";
	cd ${d}; git pull origin master; git push origin master; cd ..;
	echo "Done-----------------------------------";
}

for d in `ls`; do 
	repo="$d/.git"
	if [ -d $repo ]; then
	  repo_sync ${d}
	fi;
done
