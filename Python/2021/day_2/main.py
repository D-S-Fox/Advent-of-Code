'''
AUTHOR: Dylan Fox
DATE: 1-5-22

Day URL: https://adventofcode.com/2021/day/2

'''

f = open("input.txt", "r")
raw_lines = f.readlines()
lines = [] # Iterable list

for i in range(len(raw_lines)): # Formats input
    if "\n" in raw_lines[i]:
        lines.append(str(raw_lines[i])[:-1])


####################################################
#--- Part One ---
####################################################
def part_one():
    x = 0
    y = 0
    
    for i in range(len(lines)):
        num = int(lines[i][-1])

        if "forward" in lines[i]:
            x += num
        elif "up" in lines[i]:
            y -= num
        elif "down" in lines[i]:
            y += num
    print(f"Part 1 answer: {x * y}") 
    #print(f'{up} - {down} - {forward}')

####################################################
#--- Part Two ---
####################################################
def part_two():
    x, y, aim = 0, 0, 0

    for i in range(len(lines)):
        num = int(lines[i][-1])

        if "forward" in lines[i]:
            x += num
            if aim != 0:
                y += num * aim              
        elif "up" in lines[i]:
            #y -= num
            aim -= num        
        elif "down" in lines[i]:
            #y += num
            aim += num
    print(f'Part 2 answer: {x * y}') 

part_one()
part_two()