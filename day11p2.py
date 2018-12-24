#12/24/2018
#Find the square which has the largest total power, the square can be anywhere from 1x1 to 300x300

#The package numpy has some tools that can help with the multidimensional arrays and creating the summed area table
#Note that numpy uses matrix indexing (i,j / row,col) vs cartesian indexing (x,y) --> if the matrix is printed out, it will be "rotated"
import numpy as np


#Puzzle input
serialNum = 9995



def calcCellPower(x,y,serialNum):
	rackID = x + 10
	value = ((y * (x + 10)) + serialNum) * rackID

	#Keep the hundredths digit
	s = str(value) 
	hundreds = int(s[len(s)-3])

	powerLevel = hundreds - 5

	return powerLevel



def calcAreaPower(x,y,s):
	#Need to bound these params - if we are on the edge (ie, 0) will index outside the table!
	#This method will probably cause issues if the solution is near the edge of the grid, but works for the problem here
	if x == 0:
		x = 1
	
	if y == 0:
		y = 1
	
	#Must subtract 1 from the size (s) since the grid size is inclusive; ie, if the grid is 3x3, adding 3 would check a grid that is 4x4
	power = sumTable[x+(s-1)][y+(s-1)] + sumTable[x-1][y-1] - sumTable[x-1][y+(s-1)] - sumTable[x+(s-1)][y-1]
	return power	



#Create fuel grid: 300x300, use ints (defaults to float)
fuelGrid = np.zeros(shape=(300,300),dtype=int)

#Populate the values in the fuelGrid
for x in range(300):
	for y in range(300):
		fuelGrid[x][y] = calcCellPower(x+1, y+1, serialNum)

#Calculate summed area table
sumTable = fuelGrid.cumsum(axis=0).cumsum(axis=1)


#Find the square with the highest power rating, it is identified by the x,y coordinate in the upper left corner
max = 0
for s in range(299):
	for x in range(300-s):
		for y in range(300-s):
			sum = calcAreaPower(x,y,s)
			if sum > max:
				max = sum
				#Add one to the answer since the matrix starts from 0
				loc = x+1,y+1,s
				##print("new max:",max,loc)
		
print("Largest total power:",loc)
print("Total power:",max)



''' MISC

Correct answer: 233,116,15 


#print a partial grid
for x in range(10):
	print(fuelGrid[x][:10])
	
	
	
'''