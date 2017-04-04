#!/bin/bash

filename="../URL_list.csv"
mkdir -p html2

while read -r line
do
	#State Code;State;Dist Code;Dist;Page
	scode=$( echo "$line" |cut -d\, -f1 )
	sname=$( echo "$line" |cut -d\, -f2 )
	dcode=$( echo "$line" |cut -d\, -f3 )
	dname=$( echo "$line" |cut -d\, -f4 )

	durl="Constituencywise$scode$dcode.htm"
	fname="$scode-$dcode-$sname-$dname"
	echo Converting file $durl ------------- $fname
	#touch html/$fname.html
	#wget "http://eciresults.nic.in/"$durl -O html/$fname.html
	cat html/$fname.html | pup '#div1' > html2/$fname.html
	#pandoc -s -r html html/$fname.html -o md/$fname.md

done < "$filename"
