#2/15/2020
#Use the code from the first puzzle to calculate the inputs needed to get 19690720


#Open the input file and read the data
input = open("input.txt")
data = input.read()


def calc_intcode(noun, verb):
    #Load the array into memory
    intcode = data.split(',')

    #Initialize the list inputs
    intcode[1] = str(noun)
    intcode[2] = str(verb)

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

    return intcode[0]



for noun in range(0,99):
    for verb in range(0,99):
        if calc_intcode(noun,verb) == 19690720:
            print(100 * noun + verb)            



#Correct answer: 7960