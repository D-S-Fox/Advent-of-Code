'''
AUTHOR: Dylan Fox
DATE: 1-5-22

Day URL: https://adventofcode.com/2021/day/3

'''

f = open("input.txt", "r")
raw_lines = f.readlines()
#lines= [] # Iterable list
lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"] 

for i in range(len(raw_lines)): # Formats input
    if "\n" in raw_lines[i]:
        pass#lines.append(str(raw_lines[i])[:-1])

####################################################
#--- Part One ---
####################################################
def binaryToDecimal(n):
    return int(n,2)

def part_one():
    gamma_rate = "" # Most common
    epsilon_rate = "" # Least common
    bit_pos = 0

    while bit_pos <= len(lines[0])-1:
        on_bit, off_bit = 0, 0

        for i in range(len(lines)):

            if int(lines[i][bit_pos]) == 1:
                on_bit += 1
            else:
                off_bit += 1
                    
        if on_bit > off_bit:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
        bit_pos += 1

    gama_decimal = binaryToDecimal(gamma_rate)
    epsilon_decimal = binaryToDecimal(epsilon_rate)

    print(gama_decimal * epsilon_decimal)
    
    part_two(gamma_rate, epsilon_rate)

    


####################################################
#--- Part Two ---
#################################################### 
# PLAN
# USE THE .REMOVE FUNCTION????
# Use gamma/epsilon_rate variables from previous part??
# Iterate through whole list and remove non matching elements?
def part_two(gamma_rate, epsilon_rate):
    cut_list = lines  
    oxygen_generator = "" # Most common
    co2_scrubber = "" # Least common

    current_bit = 0
    while cut_list != 1:
        for i in range(len(cut_list)):
            if cut_list[i][current_bit] != gamma_rate[current_bit]:
                print(cut_list)
        current_bit += 1
        


part_one()