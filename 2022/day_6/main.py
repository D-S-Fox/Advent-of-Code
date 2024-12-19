def puzzle1(data):
    ANSWER = 0 
    for i in range(len(data)-4):
        compareChars = data[i:i+4]
        if len(compareChars) == len(set(compareChars)): # Compares length of list vs length of list with duplicate characters removed
            ANSWER = i+4
            break
    print(f'Day one answer: {ANSWER}')

def puzzle2(data):
    ANSWER = 0
    for i in range(len(data)-14):
        compareChars = data[i:i+14]
        if len(compareChars) == len(set(compareChars)): # Compares length of list vs length of list with duplicate characters removed
            ANSWER = i+14
            break
    print(f'Day two answer: {ANSWER}')

def getinput():
    array = []
    with open("input.txt") as infile:
        for line in infile:
            line = line.strip()
            for letter in line:
                array.append(letter)
        return array


def main():
    rawinput=getinput()
    #print(rawinput[:5])
    puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()