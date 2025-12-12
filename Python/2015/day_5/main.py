"""

"""
import os.path
from time import perf_counter

def puzzle1(data):
    start_time = perf_counter()
    puzzle1_answer = "Lost the code??"


    print(f'Puzzle 1 Answer: {puzzle1_answer}')
    end_time = perf_counter()
    print(f"Puzzle 1 processed in {end_time - start_time:.8f} seconds.\n")

def letter_pair(line):
    for i in range(len(line)-1):
        current_pair = line[i] + line[i+1]
        if current_pair in line[i+1:]:
            print(f"- {current_pair}")
            return True
    
    return False

def letter_repeat(line):
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            return True
        
    return False

def puzzle2(data):
    start_time = perf_counter()
    puzzle2_answer = 0

    for line in data:
        print(line)
        rule_1=letter_pair(line)
        if rule_1:
            rule_2=letter_repeat(line)
            if rule_2:
                puzzle2_answer += 1

    print(f'Puzzle 2 Answer: {puzzle2_answer}')
    end_time = perf_counter()
    print(f"Puzzle 2 processed in {end_time - start_time:.8f} seconds.\n")

def get_input():
    # Gets scripts absolute path and changes to its directory
    start_time = perf_counter()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as infile:
    #with open("testinput.txt") as infile:
        end_time = perf_counter()
        print(f"Got input in {end_time - start_time:.8f} seconds.\n")
        return infile.read().splitlines()
        
def format_data(raw_input):
    start_time = perf_counter()



    end_time = perf_counter()
    print(f"Formated data in {end_time - start_time:.8f} seconds.\n")
    return (raw_input)


def main():
    raw_input=get_input()
    #print(raw_input)
    data=format_data(raw_input)
    #print(data)
    puzzle1(data)
    puzzle2(data)

if __name__ == "__main__":
    main()
