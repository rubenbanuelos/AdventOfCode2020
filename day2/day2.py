# Advent of code 2020 - Day 2

import re

f = open("input", "r")

total = 0

for a in f:
	line = re.split(":",a)
	restriction = line[0]
	password    = line[1][1:]

	password.strip

	low  = int(re.split("-",(re.split(" ",restriction)[0]))[0])
	high = int(re.split("-",(re.split(" ",restriction)[0]))[1])
	buchstabe = re.split(" ",restriction)[1]

	if (password[low-1] == buchstabe)^(password[high-1] == buchstabe):
		total += 1

print(total)