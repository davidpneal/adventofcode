#12/2/2018
#This puzzle checks a series of strings for letters that are repeated twice and for letters that are repeated thrice or more.
#At the end, these two counters are multiplied to generate a basic checksum. Count a double or triple only once per string.

input = open("d02-1input.txt")
#input = open("d02-1test.txt")
data = input.read()

boxid = []
#The splitlines method will split the string on the newline characters
for line in data.splitlines():
	boxid.append(line)

doubles = 0
triples = 0	

#Process the list of strings
for id in boxid:
	
	#The fromkeys method will create a dictionary with keys from the string (each unique character is a key)
	tally = dict.fromkeys(id, 0)
	
	#Count up each characters occurrence
	for char in id:
		tally[char] += 1
	
	if 2 in tally.values():
		doubles += 1
	
	if max(tally.values()) >= 3:
		triples +=1

#print(doubles)
#print(triples)

print("Checksum:",doubles * triples)

	
	
	
''' MISC

Correct answer: 6696


sorted(var) - will sort the characters of the string into a list, can also join them to make a string again

#Can use a also default dict to count items; if the key is missing, it will automatically add it to the collection
import collections
dict = collections.defaultdict(int)
for char in line:
	dict[char] += 1
	
#Dump the values in the dictionary as a list
values = list(tally.values())
	
	
'''

