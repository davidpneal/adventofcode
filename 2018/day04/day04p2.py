#12/4/2018
#This script analyzes sleep logs to identify which 'guard' sleeps the most for any given minute

from datetime import datetime
from collections import defaultdict

input = open("day04input.txt")
#input = open("day04test.txt")
data = input.read()

log = []
for line in data.splitlines():
	log.append(line)
	
chrono = []
for line in log:
	d = datetime.strptime(line[0:18], '[%Y-%m-%d %H:%M]')
	msg = line[19:]
	#Append the tuple pair
	chrono.append((d,msg))
	
#Sort the list by datetime
chrono.sort()


#defaultdict will create new keys if they don’t already exist
sleepdict = defaultdict(list)

#Accumulate the wake and sleep times for each guard
#Note: this structure will not correctly handle sleep time spans that begin before 0 or end after 59
for log in chrono:
	#Get the first 5 letters of the message
	if log[1][:5] == "Guard":
		#log[1] is the message, the numerical part of the message starts at char 8, 
		# split the str to get the first character group (the number) then convert it to int()
		currguard = int(log[1][7:].split()[0])
		continue
	elif log[1][:5] == "falls":
		sleeptime = log[0].minute
		continue
	else:
		log[1][:5] == "wakes"
		waketime = log[0].minute
		
	#Once a waketime is found, we have a full set of data - add it to the dataset for that guard
	sleepdict[currguard].append(sleeptime)
	sleepdict[currguard].append(waketime)
	
	
#Check each guard to see how much they sleep for each minute, save the largest value

#Data: guard, minute, count
topsleeper = (0,0,0)

for guard in sleepdict:
	breakdown = defaultdict(int)
	
	#Count by twos up to the length of the list associated with guard
	for n in range(0,len(sleepdict[guard]),2):
		for i in range(sleepdict[guard][n],sleepdict[guard][n+1]):
			breakdown[i] += 1
	
	#Find the key with the largest value~ max(iterable, key) - key describes how to compare elements
	#The lambda <item>: return <a result of operation with item> ~ get the value for the key
	minute = max(breakdown, key=lambda k: breakdown[k])
	count = max(breakdown.values())
	
	#If the currently analyzed guard slept more than the old record holder, update topsleeper
	if(count >= topsleeper[2]):
		topsleeper = (guard, minute, count)	
		
	
print("Guard:", topsleeper[0])
print("Count:", topsleeper[2])
print("Minute:", topsleeper[1])
print("Guard x Minute:",topsleeper[0] * topsleeper[1])
	
	
	
	

''' MISC

Correct answer: 65474



	
'''