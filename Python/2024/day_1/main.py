import os

def splitSortList(data):
    leftColumn = []
    rightColumn = []

    for i in data:
        tmp = (i.split('   '))
        leftColumn.append(tmp[0])
        rightColumn.append(tmp[1])

    #print(leftColumn)
    #print(rightcolumn)

    leftColumn.sort()
    rightColumn.sort()

    return leftColumn, rightColumn

def puzzle1(data):
    leftColumn, rightColumn = splitSortList(data)

    totalDistance = 0

    for i in range(len(leftColumn)):
        distance = int(leftColumn[i]) - int(rightColumn [i])
        totalDistance += abs(distance)
        
        #print(f"{leftColumn[i]} - {rightColumn[i]} = {distance}")

    print(f"Total distance: {totalDistance}")

def puzzle2(data):
    leftColumn, rightColumn = splitSortList(data)

    similarityScore = 0

    for i in leftColumn:
        numOfMatches = 0
        for j in rightColumn:
            if i == j:
                numOfMatches += 1
        similarityScore += int(i) * numOfMatches
    
    print(f"Similarity Score: {similarityScore}")

def getinput():
    array = []

    # Gets scripts absolute path and changes to its directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

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