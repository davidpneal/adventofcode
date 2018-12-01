#12/1/2018

#Open the input file and read the data
input = open("d01-1input.txt")
data = input.read()

total = 0

#The splitlines method will split the string on the newline characters
for value in data.splitlines():
	total += int(value)

print(total)
	
	
''' MISC
To move this data into a list:

#Initalize an empty list
frequencies = []

for line in data.splitlines():
	frequencies.append(int(line))

	
Correct answer: 525
'''