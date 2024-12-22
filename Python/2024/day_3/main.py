import os
import re

def puzzle1(data):
    puzzle1_answer = 0

    find_muls = re.findall("mul\(\d+,\d+\)", str(data))

    for i in range(len(find_muls)):
        nums = re.findall("\d+", find_muls[i])
        puzzle1_answer += (int(nums[0]) * int(nums[1]))

    print(f'Puzzle 1 Answer: {puzzle1_answer}')

def puzzle2(data):
    puzzle2_answer = 0

    find_args = re.findall("do\(\)|don\'t\(\)|mul\(\d+,\d+\)", str(data))

    mul_inst = 1

    for i in range(len(find_args)):
        print(find_args[i])
        if find_args[i] == "do()":
            mul_inst = 1
        elif find_args[i] == "don't()":
            mul_inst = 0
        else:
            pass
        
        if mul_inst == 1 and any(char.isdigit() for char in find_args[i]):
            nums = re.findall("\d+", find_args[i])
            puzzle2_answer += (int(nums[0]) * int(nums[1]))
        else:
            pass

    print(f'Puzzle 2 Answer: {puzzle2_answer}')

def getinput():
    array = []

    # Gets scripts absolute path and changes to its directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as infile:
        return infile.readlines()


def main():
    rawinput=getinput()
    #print(rawinput)
    puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()