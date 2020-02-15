#2/15/2020

#Open the input file and read the data
input = open("input.txt")

#Load the array into memory
data = input.read()
intcode = data.split(',')

#List initial adjustment, comment these out for the test data set
intcode[1] = '12'
intcode[2] = '2'

index = 0
while index < len(intcode):
    #Populate the position values for the current opcode (4 list element block)
    opcode = intcode[index]
    posin1 = int(intcode[index+1])
    posin2 = int(intcode[index+2])
    posout = int(intcode[index+3])

    if opcode == '1':
        intcode[posout] = int(intcode[posin1]) + int(intcode[posin2])
        #print("Add the values", intcode[posout])

    elif opcode == '2':
        intcode[posout] = int(intcode[posin1]) * int(intcode[posin2])
        #print("Multiply the values", intcode[posout])

    elif opcode == '99':
        break

    else:
        print("Error: unexpected value:", opcode)
        exit

    index += 4

print(intcode[0])

#Correct answer: 3224742