#12/1/2018
#This puzzle requires looping through a list of numbers (negative and positive) and summing them;
# the goal is to identify the first value in the running total the program reaches twice

#Open the input file and read the data
input = open("d01-1input.txt")
#input = open("d01-2test.txt")
data = input.read()

#Initialize an empty list that will be populated with the data
frequencies = []

#The splitlines method will split the string on the newline characters
for line in data.splitlines():
	frequencies.append(int(line))

#Create a dictionary to store the results, this will take more memory but be much faster than a list
#Some trial and error with the dataset gave a working size of -200k to 200k
#A dictionary comprehension can create the dictionary with all key values initialized to 0
dict = {n:0 for n in range(-200000,200001)}

total = 0
loopcount = 0
loop = True

#Create a loop to repeat frequencies until a repeated value is found
while loop:
	loopcount += 1
	
	#Loop through the frequencies list
	for value in frequencies:
		total += value
		
		#Using the current total as the key, add one to the value
		dict[total] += 1
		
		#Check if there is a repeat
		if dict[total] == 2:
			print(total,"has been repeated")
			loop = False
			break

print("Finished on loop",loopcount)

	
	
''' MISC

Get the length of a list: len(frequencies)

Correct answer: 75749

~~~
Reviewing other solutions; it looks like a set would be a cleaner implementation;
solves issue where the table might not be correctly sized for the input dataset

'''