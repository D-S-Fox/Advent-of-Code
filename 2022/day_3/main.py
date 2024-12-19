import string

def puzzle1(data):
    alphabetScore = '0' + str(string.ascii_letters) # 0 added to front as null so scores match index
    commonItems = ['0']
    ANSWER = 0  
    for i in range(len(data)):
        # Gets current RUCKSACK and splits into two COMPARTMENTS
        rucksack = data[i]
        mid = int(len(rucksack) / 2)
        compartment1 = rucksack[:mid]
        compartment2 = rucksack[mid:]

        # Parses both compartments and compares like characters
        for i in range(len(compartment1)):
            for j in range(len(compartment2)):
                if compartment1[i] == compartment2[j]:
                    commonItems.append(compartment1[i])
                    break
            else:
                continue # only executed if the inner loop did NOT break
            break # only executed if the inner loop DID break

    # Parses commonItems and adds priority to ANSWER
    for i in range(len(commonItems)):
        for j in range(len(alphabetScore)):
            if commonItems[i] == alphabetScore[j]:
                #print("Adding " + str(j))
                ANSWER += j

    print(f'Part 1 answer: {ANSWER}')

def puzzle2(data):
    alphabetScore = '0' + str(string.ascii_letters) # 0 added to front as null so scores match index
    commonItems = ['0']
    ANSWER = 0  

    # Break input into groups and find comming item between them
    group = []
    for i in range(len(data)):
        if i % 3 == 0: # Breaks data into groups of three
            group = data[i:i+3]
        elif len(group) == 3: # If list is full / iterate through and find common item
            #print(f'{group[0]}\n{group[1]}\n{group[2]}\n')
            for w in set(group[0]):
                if w in group[1]:
                    if w in group[2]:
                        commonItems.append(w)
            group.clear() # Clears list


    # Parses commonItems and adds priority to ANSWER
    for i in range(len(commonItems)):
        for j in range(len(alphabetScore)):
            if commonItems[i] == alphabetScore[j]:
                #print("Adding " + str(j))
                ANSWER += j

    print(f'Part 2 answer: {ANSWER}')


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