"""

"""

def puzzle1(data):
    pass

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