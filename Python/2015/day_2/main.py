'''
AUTHOR: Dylan Fox
DATE: 1-6-22

Day URL: https://adventofcode.com/2015/day/2

'''

f = open("input.txt", "r")
raw_lines = f.readlines()
lines = [] # Iterable list

for i in range(len(raw_lines)): # Formats input
    if "\n" in raw_lines[i]:
        lines.append(str(raw_lines[i])[:-1])

####################################################
#--- Part One ---

# Does the math
def calculate_sqft(l, w, h):
    extra = 1000
    sides = [l*w, w*h, h*l]

    # Finds smallest side and saves it in extra variables
    for i in range(len(sides)):
        if int(sides[i]) < extra:
            extra = sides[i]
    surface_area = (2*sides[0]) + (2*sides[1]) + (2*sides[2])
    return (surface_area + extra)
    

def part_one():
    sqr_feet = 0

    # Splits measurement string and passes to calculate
    for i in range(len(lines)):
        stack = lines[i]
        l, w, h = stack.split('x')
        sqr_feet += calculate_sqft(int(l), int(w), int(h))
    print(f"Total sqft: {sqr_feet}")


        

####################################################
#--- Part Two ---

# Calucated total feet of ribbon per box
def calculate_ribbon(l, w, h):
    sides = [l, w, h]    
    bow = (sides[0] * sides[1] * sides[2])

    # Sorts list and pops off last value(highest)
    small_sides = sides
    small_sides.sort()
    small_sides.pop()
    
    return ((small_sides[0]*2) + (small_sides[1]*2)) + bow

def part_two():
    feet_of_ribbon = 0

    for i in range(len(lines)):
        stack = lines[i]
        l, w, h = stack.split('x')
        feet_of_ribbon += calculate_ribbon(int(l), int(w), int(h))
    print(f"Total ribbon in feet: {feet_of_ribbon}") 



part_one()
part_two()