#12/4/2018
#This script analyzes sleep logs to identify which 'guard' sleeps the most then
# identifies which minute in the hour they are asleep the most frequently

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
	
	
#Count up the sleep time for each guard
topsleeper = (-1,0)
for guard in sleepdict:
	sleeptime = 0
	for n in range(0,len(sleepdict[guard]),2):
		sleeptime += sleepdict[guard][n+1] - sleepdict[guard][n]
	
	#If the currently analyzed guard slept more than the old record holder, update topsleeper
	if(sleeptime > topsleeper[1]):
		topsleeper = (guard, sleeptime)
	

#Tally how much the guard was sleeping for each minute
guard = topsleeper[0]
breakdown = defaultdict(int)

#Same code as above, count by twos up to the length of the list associated with guard
for n in range(0,len(sleepdict[guard]),2):
	for i in range(sleepdict[guard][n],sleepdict[guard][n+1]):
		breakdown[i] += 1

		
#Find the key with the largest value~ max(iterable, key) - key describes how to compare elements
#The lambda <item>: return <a result of operation with item> ~ get the value for the key
mostsleep = max(breakdown, key=lambda k: breakdown[k])

print("Guard x Minute:",guard * mostsleep)




''' MISC

Correct answer: 39422



	
'''