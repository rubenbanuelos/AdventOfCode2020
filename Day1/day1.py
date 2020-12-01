#First day advent of code

entries = []

f = open("input", "r")

for x in f:
	entries.append(int(x))

for a in entries:
	entries.remove(a)
	for b in entries:
		if a + b == 2020:
			respuesta = a*b

print(respuesta)