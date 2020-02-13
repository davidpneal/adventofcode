#12/16/2018
#This program parses a tree of numbers in format: Node = CMcm; C = number of children, M = number of metadata,
# c = zero or more child nodes, m = zero or more metadata numbers.  
#Find the value of the tree using a couple of different methods to calculate the value.

input = open("day08input.txt")
#input = open("day08test.txt")



def parsenode(array, startindex):
	numChildren = int(array[startindex])
	numMetadata = int(array[startindex + 1])
	sumdata = 0
	
	if numChildren != 0:
		#Create the list to track the value of the children, populate element 0 to simplify lookups
		child = [0]
		
		for i in range(numChildren):
			child.append(parsenode(array, startindex + 2))
		
		#The value of a node with children is the sum of the children as selected by the numMetadata values
		#ie, if the metadata is 1, get the value of the first child and add it to the sum for that node
		for x in array[startindex+2:(startindex+2+numMetadata)]:
			if len(child) > int(x):
				sumdata += child[int(x)]
			
	else:
		#For nodes that have no children, sum the value of the metadata which is the next numMetadata after the header
		for x in array[startindex+2:(startindex+2+numMetadata)]:
			sumdata += int(x)

	#Delete the header and metadata
	del array[startindex:startindex+2+numMetadata]
	
	return sumdata


	
data = list(input.read().split())
total = parsenode(data,0)

print("Sum of metadata numbers:",total) 

	
	
	
	

''' MISC

Correct answer: 13935


'''