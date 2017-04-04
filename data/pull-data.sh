#!/bin/bash

filename="../URL_list.csv"
mkdir -p html

while read -r line
do
	#State Code;State;Dist Code;Dist;Page
	scode=$( echo "$line" |cut -d\, -f1 )
	sname=$( echo "$line" |cut -d\, -f2 )
	dcode=$( echo "$line" |cut -d\, -f3 )
	dname=$( echo "$line" |cut -d\, -f4 )

	durl="Constituencywise$scode$dcode.htm"
	fname="$scode-$dcode-$sname-$dname"

	echo Downloading file $durl ------------- $fname
		#touch html/$fname.html
	wget "http://eciresults.nic.in/"$durl -O html/$fname.html

	sleep 0.5

done < "$filename"
