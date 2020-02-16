#2/16/2020
#Ruby version of the solution

#Read the data from the input file
$input = File.read("input.txt")


def calc_intcode(noun, verb)
    #Load the array into memory, converting to to integers
    intcode = $input.split(',').map(&:to_i)

    #Initialize the list inputs
    intcode[1] = noun
    intcode[2] = verb

    index = 0
    loop do
        #Populate the position values for the current opcode (4 list element block)
        opcode = intcode[index]
        posin1 = intcode[index+1]
        posin2 = intcode[index+2]
        posout = intcode[index+3]

        case opcode 
        when 1
            intcode[posout] = intcode[posin1] + intcode[posin2]
            #puts "Add the values, result = #{intcode[posout]}"

        when 2
            intcode[posout] = intcode[posin1] * intcode[posin2]
            #puts "Multiply the values, result = #{intcode[posout]}"

        when 99
            break

        else
            puts "Error: unexpected value: #{opcode}"
            exit  
        end

        index += 4
    end

    return intcode[0]
end


for noun in 0..99 do 
    for verb in 0..99 do
        if calc_intcode(noun,verb) == 19690720
            puts 100 * noun + verb            
        end
    end
end


#Correct answer: 7960