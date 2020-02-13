#12/8/2018
#This script determines the dependency graph for a simple set of "A before B" type data

from collections import defaultdict

input = open("day07input.txt")
#input = open("day07test.txt")

#Graph keeps a list of the prereqs for each step, allsteps keeps track of all possible steps
graph = defaultdict(list)
allsteps = set()

for line in input.read().splitlines():
	data = line.split()
	#Element 7 is the key and element 1 is the prereg for it
	graph[data[7]].append(data[1])
	allsteps.add(data[7])
	allsteps.add(data[1])

	
results = []

#Any items that aren't in the dict have no prereqs; get these with difference and convert them to a list
ready = list(allsteps.difference(graph.keys()))

while len(ready) != 0:
	ready.sort()
	next = ready.pop(0)
	results.append(next)
	
	#Enumerate graph to delete the step that was just added to the result
	for index,reqs in enumerate(graph.values()):
		for i,step in enumerate(reqs):
			if step == next:
				currkey = list(graph.keys())[index]
				del graph[currkey][i]
				
				#if the list is now empty, remove that key
				if(len(graph[currkey]) == 0):
					ready.append(currkey)
					#The next line throws an error - resizing the dict during enumeration doesn't work
					# however, the empty list doens't affect the output so this doesn't need to be fixed
					#del graph[currkey]
					
print(''.join(results))


	

''' MISC

Correct answer: BHRTWCYSELPUVZAOIJKGMFQDXN


			
for x in sorted(graph):
    x, graph[x]
	
	
'''

