#12/16/2018
#This program parses a tree of numbers in format: Node = CMcm; C = number of children, M = number of metadata,
# c = zero or more child nodes, m = zero or more metadata numbers.  Find the sum of the metadata numbers.

input = open("day08input.txt")
#input = open("day08test.txt")



def parsenode(array, startindex):
	numChildren = int(array[startindex])
	numMetadata = int(array[startindex + 1])
	sumdata = 0
	sumchildnodes = 0
	
	if numChildren != 0:
		for i in range(numChildren):
			sumchildnodes += parsenode(array, startindex + 2)
		
	#Sum the value of the metadata which is the next numMetadata after the header
	##print("Metadata, no children:",array[startindex+2:(startindex+2+numMetadata)])
	for x in array[startindex+2:(startindex+2+numMetadata)]:
		sumdata += int(x)

	#Delete the header and metadata
	del array[startindex:startindex+2+numMetadata]
	
	return sumdata + sumchildnodes


	
data = list(input.read().split())
total = parsenode(data,0)

print("Sum of metadata numbers:",total) 

	
	
	
	

''' MISC

Correct answer: 38722


'''