#12/13/2018
#This script determines the dependency graph for a simple set of "A before B" type data
# and adds a timing component to determine the total process time

from collections import defaultdict

input = open("day07input.txt")
#Note, if using the test data set, change the default value of the dict to 0 (from 60)
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

#Any items that aren't in the dict have no prereqs; get these with difference and convert them to a list
ready = list(allsteps.difference(graph.keys()))


#Each step (A-Z) takes 60 plus one second per letter to perform
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stepsec = dict.fromkeys(alpha, 60)
#x is a generator; each time next(x) is called, it will return the next value in the iteration
x = (i for i in range(1,27))
for k in stepsec.keys():
	stepsec[k] += next(x)

#Use a multidimensional array to store the current step [0] and time remaining [1] for 5 workers
worker = [[None,0] for x in range(5)]

timer = 0
wip = 1 #need a value over 0 to enter the loop


while wip > 0:
	wip = 0
	skiptime = 100
	#sort ready since any currently ready steps should be done in alpha order
	ready.sort()
	
	for w in range(5):
		#If the worker doesnt have a task, get one from ready and assign the time from the dictionary
		if worker[w][0] == None:
			if len(ready) > 0:
				worker[w][0] = ready.pop(0)
				worker[w][1] = stepsec[worker[w][0]]
				##print("Add task to worker:", w, "Step:", worker[w][0], "Seconds:", worker[w][1])
		
		#Keep the process time of the worker with the minimum remaining process time
		if worker[w][1] < skiptime and worker[w][0] != None:
			skiptime = worker[w][1]
			##print("Setting skiptime to:",skiptime)
			
		#Work in progress is used to control the loop (only add the time if the worker has a task)
		if worker[w][0] != None:
			wip += worker[w][1]
		
	for w in range(5):
		worker[w][1] -= skiptime
		if worker[w][1] == 0: ##in theory, this shouldnt go negative
			#Enumerate graph to delete the completed step
			for index,reqs in enumerate(graph.values()):
				for i,step in enumerate(reqs):
					if step == worker[w][0]:
						currkey = list(graph.keys())[index]
						del graph[currkey][i]
				
						#if the list is now empty, remove that key
						if(len(graph[currkey]) == 0):
							ready.append(currkey)
			
			worker[w][0] = None
	
	timer += skiptime
	##print("Adding:",skiptime,"to timer.")
	
	
#The loop runs one extra time so the result is high by 100
print(timer-100)

	

''' MISC

Correct answer: 959



'''