#12/15/2018

## This version is BROKEN!


#This program parses a tree of numbers in format: Node = CMcm; C = number of children, M = number of metadata,
# c = zero or more child nodes, m = zero or more metadata numbers.  Find the sum of the metadata numbers.

#The default Python recursion depth is 1000 which is insufficient for this dataset
import sys
sys.setrecursionlimit(3000)

#input = open("day08input.txt")
input = open("day08test2.txt")

def parsenode(array):
	numChildren = int(array[0])
	numMetadata = int(array[1])
	sumdata = 0
	sumchildnodes = 0
	
	##print("numChildren:",numChildren,"numMetadata:",numMetadata)
	
	if numChildren == 0:
		#Sum the value of the metadata which is the next numMetadata after the header
		##print("Metadata, no children:",array[2:(2+numMetadata)])
		for x in array[2:(2+numMetadata)]:
			sumdata += int(x)
		
		#Generate the new array by removing 2 (header len) + numMetadata elements from the front of the list
		shortarray = list(array[(2+numMetadata):])
		##print("Short array 1",shortarray)
			
	else:
		#Sum the value of the metadata elements which are the last numMetadata elements in the list
		
		'''INCORRECT ASSUMPTION - the metadata is at the end of any children, not at the VERY end of the list'''
		
		#Skip this step if there isnt any metadata
		if numMetadata != 0:
			##print("Metadata:",array[-numMetadata])
			for x in array[-numMetadata:]:
				sumdata += int(x)
		
			#Remove the node header (first 2 elements) and the metadata (last numMetadata elements)
			#Need to generate a new list by running the results of the list slice through list() again
			#If you dont do this, shortlist will be a pointer pointing to the original list
			shortarray = list(array[2:-numMetadata])
			##print("Short array 2",shortarray)
		else:
			shortarray = list(array[2:])
			##print("Short array 3",shortarray)
		
	if len(shortarray) > 0:
		sumchildnodes = parsenode(shortarray)
	
	
	
	if numChildren == 0:
		print("Metadata, no children:",array[-numMetadata])
	else:
		print("Metadata:",array[-numMetadata])
		
	print("sumdata:",sumdata,"sumchildnodes", sumchildnodes)
	return sumdata + sumchildnodes
	
	
	


data = list(input.read().split())
total = parsenode(data)

print("Sum of metadata numbers:",total) 

	
