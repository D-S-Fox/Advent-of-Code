'''
AUTHOR: Dylan Fox
DATE: 1-5-22

Day 1 URL: https://adventofcode.com/2021/day/1

'''

f = open("input.txt", "r")
raw_lines = f.readlines()
lines = [] # Iterable list

for i in range(len(raw_lines)): # Formats input
    if "\n" in raw_lines[i]:
        str(raw_lines[i])
        lines.append(str(raw_lines[i])[:-1])

# --- Part One ---
num_of_increase = 0
for i in range(len(lines)-1):
    if int(lines[i]) < int(lines[i+1]):
        num_of_increase += 1   
print(num_of_increase)

# --- Part Two ---
num_of_window_increase = 0
old_window = 0
new_window = 0
for i in range(len(lines)-2):
    new_window = int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) # Adds three indexs
    if new_window > old_window and old_window != 0:
        num_of_window_increase += 1
    old_window = new_window
print(num_of_window_increase)
