#12/23/2018
#Find the 3x3 square which has the largest total power

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
	
	

#Create fuel grid: 300x300
fuelGrid = [([0] * 300) for x in range(300)]

#Populate the values in the fuelGrid
for x in range(300):
	for y in range(300):
		fuelGrid[x][y] = calcCellPower(x+1, y+1, serialNum)

#Find the 3x3 cell with the highest power rating, the cell is identified by the x,y coordinate in the upper left corner
max = 0
for x in range(297):
	for y in range (297):
	
		sum = 0
		for sumx in range(x,x+3):
			for sumy in range(y,y+3):
				sum += fuelGrid[sumx][sumy]
		
		if sum > max:
			max = sum
			loc = x+1,y+1
			
print("Largest total power:",loc)
print("Total power:",max)


''' MISC

Correct answer: 33,45 


	
'''