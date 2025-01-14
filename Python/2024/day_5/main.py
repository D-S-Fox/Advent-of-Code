"""

"""
import os

def puzzle1(data):
    puzzle1_answer = 0


    print(f'Puzzle 1 Answer: {puzzle1_answer}')

def puzzle2(data):
    puzzle2_answer = 0


    print(f'Puzzle 2 Answer: {puzzle2_answer}')

def getinput():
    update_rules = ()
    update_procedure = []

    # Gets scripts absolute path and changes to its directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as infile:
        data = infile.read().splitlines()
        #print(data)
    
    for i in range(len(data)):
        print(data[i])

    return data

def main():
    rawinput=getinput()
    #print(rawinput)
    puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()