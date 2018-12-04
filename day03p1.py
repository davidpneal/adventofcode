#12/3/2018
#This puzzle tracks rectangles placed on a grid to see how many of them overlap

input = open("day03input.txt")
#input = open("day03test.txt")
data = input.read()

claims = []
for line in data.splitlines():
	claims.append(line)
	
	
#Create the board as a two dimensional array of size 1000 x 1000
fabric = [([0] * 1000) for x in range(1000)]


for ticket in claims:
	#Get the xpos
	xpos = int((ticket.split())[2].split(',')[0])

	#Get the ypos; the string has a colon on the end, the [:-1] syntax generates a new string
	# without that character before running it through the int() method
	ypos = int(((ticket.split())[2].split(',')[1])[:-1])

	#Get the rectangle width
	width = int(((ticket.split())[3].split('x'))[0])

	#Get the rectangle heigth
	heigth = int(((ticket.split())[3].split('x'))[1])

	#Apply the rectangle to the fabric
	for y in range(ypos,ypos+heigth):
		for x in range(xpos,xpos+width):
			fabric[x][y] += 1

	
#Find the overlaps
overlaps = 0
for row in fabric:
	overlaps += sum(i > 1 for i in row)
	
print("Overlapping claims:",overlaps)

	

''' MISC

Correct answer: 115242

#Use split to break the claim into a list, from there can use split() and int() to derive the numbers
claims[1].split() = ['#2', '@', '3,1:', '4x4']

#Print the grid
for x in range(10):
	print(fabric[x])	

	
	
'''
