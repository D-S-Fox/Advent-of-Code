def puzzle1(data):
    ANSWER = 0
    dir_LE_100000 = []
    for i in range(len(data)):
        stdOut = data[i]
        try:
            int(stdOut[0])
            fileDetails = stdOut.split()
            if int(fileDetails[0]) <= 100000:
                ANSWER += int(fileDetails[0]) 
            else:
                pass
        except: 
            pass
    print(f'Day one Answer: {ANSWER}')


def puzzle2(data):
    pass

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
    puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()