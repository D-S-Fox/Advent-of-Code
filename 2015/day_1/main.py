'''
AUTHOR: Dylan Fox
DATE: 1-6-22

Day URL: https://adventofcode.com/2015/day/1

'''

f = open("input.txt", "r")
raw_lines = f.readlines()
lines = [] # Iterable list

for i in range(len(raw_lines)): # Formats input
    if "\n" in raw_lines[i]:
        lines.append(str(raw_lines[i])[:-1])


####################################################
#--- Part One ---
    '''
    # Objective

    # Example

    '''
####################################################
def part_one():
    lines = str(raw_lines)
    lines = lines[2:-2]
    floor = 0

    for i in range(len(lines)):
        if lines[i] == "(":
            floor += 1
        else:
            floor -= 1
    print(f"Floor: {floor}")

####################################################
#--- Part Two ---
    '''
    # Objective

    # Example

    '''
####################################################
def part_two():
    lines = str(raw_lines)
    lines = lines[2:-2]
    floor = 0

    for i in range(len(lines)):
        if lines[i] == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            print(f"Basement postiion: {i+1}\nFloor: {floor}")
            break
    


part_one()
part_two()