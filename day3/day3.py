# Advent of Code 2020 - Day 3

f = open("input","r").readlines()

field_width = len(f[0])-1
down_step = 2
right_step = 1

c = 0

for a in range((round(len(f)/down_step))):
	#print(a*down_step)
	#print((a*right_step)%field_width)
	if f[a*down_step][(a*right_step)%field_width] == "#":
		c+=1
print(c)