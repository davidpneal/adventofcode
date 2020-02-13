#12/4/2018
#This script will elimiate any adjacent letters that are the same but upper / lower case
#This algo is very inefficient since the process restarts every time a match is found

#input = open("day05input.txt")
input = open("day05test.txt")
data = input.read()

#Convert the string into a list for easier manipulation
chars = list(data)

loop = True
while loop:
	loop = False
	for c in range(0,len(chars)-1):
		if chars[c] != chars[c+1] and chars[c].lower() == chars[c+1].lower():
			#print("match:",chars[c], chars[c+1], "c:", c)
			loop = True
			del chars[c+1]
			del chars[c]

			#Need to break since the list was shortened and the end index is incorrect
			#Restartig like this also solves the issue where 3 letters (or more) occur in a row (causes too many deletions)
			break
			
#The dataset has a '/n' at the end so the result is high by 1		
print(len(chars)-1)



''' MISC

Correct answer: 11310

Print the final result at as string:
print(''.join(chars))






'''


