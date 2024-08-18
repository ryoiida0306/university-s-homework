#!/bin/sh

n=1
while [ $n -lt 40 ]; do
	echo "n=$n"
	java FiboRec $n
	java FiboDP $n
	n=`expr $n + 1`
done
