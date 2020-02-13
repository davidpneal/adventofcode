#12/2/2018
#This puzzle looks for two strings that only differ by a single character then 
# returns all of the common characters shared by those strings

import itertools

input = open("d02-1input.txt")
#input = open("d02-2test.txt")
data = input.read()

boxid = []
for line in data.splitlines():
	boxid.append(line)
	
	
#itertools can replace the standard nested for loops, this syntax generates all possible 2-item combinations 
for str1, str2 in itertools.combinations(boxid, 2):	
	numdiff = 0
	
	#The zip generator returns a list of tuple pairs, enumerate adds a counter to these tuples when looping them
	#The for sets the counter to index and the characters from the tuple pair to (c1,c2)
	for index, (c1, c2) in enumerate(zip(str1, str2)):
		#Compare the two strings character by character, if there is a difference set that to diffpos
		if c1 != c2:
			diffpos = index
			numdiff += 1
			
			#If this is the second difference, move on
			if numdiff == 2:
				break
				
	#If there was exactly one difference, a match was found
	if numdiff == 1:
		#Omit the character at diffpos using slicing
		match = str1[:diffpos] + str1[(diffpos + 1):]
		print("Common letters:",match)
		break
	
	


''' MISC

Correct answer: bvnfawcnyoeyudzrpgslimtkj



'''
