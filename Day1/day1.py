#Advent of Code 2020 - Day 1

import copy

entries = []

f = open("input", "r")

for x in f:
	entries.append(int(x))

respuesta = 0

def trysum(arr,test):
	for a in arr:
		arr.remove(a)
		for b in entries:
			if a + b == test:
				return(a*b)
	return(0)

for a in entries:
	entries.remove(a)
	temp_entries = copy.copy(entries)
	test = 2020 - a
	
	resp = trysum(temp_entries, test) 

	if resp != 0:
		respuesta = resp*a
		

print(respuesta)