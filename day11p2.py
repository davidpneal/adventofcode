#12/23/2018
#Find the square which has the largest total power, the square can be anywhere from 1x1 to 300x300

#Puzzle input
serialNum = 18



def calcCellPower(x,y,serialNum):
	rackID = x + 10
	value = ((y * (x + 10)) + serialNum) * rackID

	#Keep the hundredths digit
	s = str(value) 
	hundreds = int(s[len(s)-3])

	powerLevel = hundreds - 5

	return powerLevel
	
	

def calcGridPower(size):
	max = 0
	for x in range(300-size):
		for y in range (300-size):
		
			sum = 0
			for sumx in range(x,x+size):
				for sumy in range(y,y+size):
					sum += fuelGrid[sumx][sumy]

			if sum > max:
				max = sum
				loc = x+1,y+1
	
	return x,y,sum



#Create fuel grid: 300x300
fuelGrid = [([0] * 300) for x in range(300)]

#Populate the values in the fuelGrid
for x in range(300):
	for y in range(300):
		fuelGrid[x][y] = calcCellPower(x+1, y+1, serialNum)

		
#Find the cell with the highest power rating, the cell is identified by the x,y coordinate in the upper left corner
max = 0
for s in range(299):
	print(s)
	best = calcGridPower(s)
	
	if best[2] > max:
		max = best[2]
		loc = best[0]+1,best[1]+1,s

			
print("Largest total power:",loc)
print("Total power:",max)


''' MISC

Correct answer: 


	
'''