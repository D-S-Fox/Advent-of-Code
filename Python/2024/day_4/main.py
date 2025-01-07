import os

def check_line(directional_string):
    xmas_match = 0
    
    if len(directional_string) == 0:
        return 0
    else:
        for j in range(len(directional_string)):
            if directional_string[j].upper() == 'X':
                if 'XMAS' in directional_string[j:j+4] and j+4 >= len(directional_string):
                    #print(directional_string[j:j+4])
                    xmas_match += 1
                elif 'SAMX' in directional_string[j-4:j] and j-4 >= 0:
                    #print(directional_string[j-4:j])
                    xmas_match += 1

        return xmas_match

def get_horiz_line(horiz_string):
    for j in range(len(horiz_string)):
            if horiz_string[j].upper() == 'X':
                return horiz_string[j-3:j+4]


def puzzle1(data):
    puzzle1_answer = 0

    for i in range(len(data)):
        horiz_string = data[i]

        for j in range(len(horiz_string)):
            if horiz_string[j].upper() == 'X':
                # Pull vertical string
                vert_string = ""
                for k in range(7):
                    index = k-3
                    if (i-3) < 0 or (i+3) >= len(data):
                        pass
                    else:
                        temp_string = data[i+index]
                        vert_string += (temp_string[j])
                #print(vert_string)

                # Pull the diagonal string

                puzzle1_answer += check_line(horiz_string)
                puzzle1_answer += check_line(vert_string)
                #puzzle1_answer += check_vertical(data)


    print(f'Puzzle 1 Answer: {puzzle1_answer}')

def puzzle2(data):
    puzzle2_answer = 0


    print(f'Puzzle 2 Answer: {puzzle2_answer}')

def getinput():
    array = []

    # Gets scripts absolute path and changes to its directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as infile:
        for line in infile:
            array.append(line.strip("\n"))
    
    return array


def main():
    rawinput=getinput()
    #print(rawinput)
    puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()
