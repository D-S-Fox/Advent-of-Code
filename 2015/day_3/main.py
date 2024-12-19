'''
AUTHOR: Dylan Fox
DATE: 1-6-22

Day URL: https://adventofcode.com/2015/day/3

'''

f = open("input.txt", "r")
raw_lines = f.readlines()
lines = [] # Iterable list

for i in range(len(raw_lines)): # Formats input
    if "\n" in raw_lines[i]:
        lines.append(str(raw_lines[i])[:-1])

####################################################
#--- Part One ---

def part_one(): # Incorrect: 8192 too high (not length)
    # Formats data
    lines = str(raw_lines)
    lines = lines[2:-2]

    presents_given = 1 # Tracks num of gifts given (1 for starting location)
    
    

####################################################
#--- Part Two ---

def part_two():
    pass


part_one()
part_two()