#2/14/2020
#This puzzle requires some basic numerical manipulation on a set of numbers

import math

input = open("input.txt")
data = input.read()

total = 0
for value in data.splitlines():
	total += math.floor(int(value) / 3) - 2

print("Fuel Required:", total)

#Correct answer: 3368364