import re

def puzzle1(data):
    ANSWER = 0
    for i in range(len(data)):
        pair = re.split(',|-', data[i]) # Splits pair into numbers for both elves
        if ((int(pair[0]) <= int(pair[2])) and (int(pair[1]) >= int(pair[3]))) or ((int(pair[0]) >= int(pair[2])) and (int(pair[1]) <= int(pair[3]))):
            ANSWER += 1

    print(f'Day 1 answer: {ANSWER}')

def puzzle2(data):
    ANSWER = 0
    for i in range(len(data)):        
        rangeOne = []
        rangeTwo = []
        pair = re.split(',|-', data[i]) # Splits pair into numbers for both elves

        # Append all numbers in given ranges to a list
        for x in range(int(pair[0]),int(pair[1])+1):
            rangeOne.append(x)
        for j in range(int(pair[2]),int(pair[3])+1):
            rangeTwo.append(j)

        # Evaluates if rangeLists share any items
        if any(i in rangeOne for i in rangeTwo):
            ANSWER += 1

    print(f'Day 2 answer: {ANSWER}')

def getinput():
    array = []
    with open("input.txt") as infile:
        for line in infile:
            line = line.strip('\n')
            array.append(line)
        return array


def main():
    rawinput=getinput()
    #print(rawinput)
    #puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()