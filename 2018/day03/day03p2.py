#12/3/2018
#This code finds the rectangle that doesnt overlap with any other rectangle

	
def convertclaim(input):
	result = dict()
	
	#Get the xpos
	result['xpos'] = int((input.split())[2].split(',')[0])

	#Get the ypos; the string has a colon on the end, the [:-1] syntax generates a new string
	# without that character before running it through the int() method
	result['ypos'] = int(((input.split())[2].split(',')[1])[:-1])

	#Get the rectangle width
	result['width'] = int(((input.split())[3].split('x'))[0])

	#Get the rectangle heigth
	result['heigth'] = int(((input.split())[3].split('x'))[1])
	
	return result

	
def findresult(input):
	for x in range(1000):
		for y in range(1000):
			if input[x][y] is not None:
				if input[x][y] >= 0:
					return input[x][y]
	
	

input = open("day03input.txt")
#input = open("day03test.txt")
data = input.read()

claims = []
for line in data.splitlines():
	claims.append(line)
	
	
#Create the board as a two dimensional array of size 1000 x 1000
fabric = [([None] * 1000) for x in range(1000)]


for index, ticket in enumerate(claims):

	c = convertclaim(ticket)
	overlap = False
	badclaims = set()
		
	#Check the area to be written, make sure it is unoccupied
	for y in range(c['ypos'],c['ypos']+c['heigth']):
		for x in range(c['xpos'],c['xpos']+c['width']):
			if fabric[x][y] != None:
				overlap = True
				#Add current claim to badclaims and store the claim number that caused the collision
				badclaims.add(index)
				badclaims.add(fabric[x][y])

	if overlap:
		#for each invalid claim
		for claim in list(badclaims):
			c = convertclaim(claims[claim])
			#set those claim areas to -1
			for y in range(c['ypos'],c['ypos']+c['heigth']):
				for x in range(c['xpos'],c['xpos']+c['width']):
					fabric[x][y] = -1
	else:
		#Assign the ticket to the fabric since there is no overlap
		for y in range(c['ypos'],c['ypos']+c['heigth']):
			for x in range(c['xpos'],c['xpos']+c['width']):
				fabric[x][y] = index

print("Non overlapping claim:",claims[findresult(fabric)])

	

''' MISC

Correct answer: #1046 @ 858,295: 16x21

#Use split to break the claim into a list, from there can use split() and int() to derive the numbers
claims[1].split() = ['#2', '@', '3,1:', '4x4']

#Print the grid
for x in range(10):
	print(fabric[x])

Future improvements: a couple of spots could be reduced into another function	

'''
