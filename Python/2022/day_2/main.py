# A, X = Rock
# B, Y = Paper
# C, Z = Scissors
def puzzle1(data):
    totalScore = 0
    rock, paper, scissors, draw, win = 1, 2, 3, 3, 6 # Score system
    for i in range(len(data)):
        match = data[i].split()
        # Opponent Throws Rocks
        if match[0] == 'A' and match[1] == 'X':
            totalScore += (rock + draw)
        elif match[0] == 'A' and match[1] == 'Y':
            totalScore += (paper + win)
        elif match[0] == 'A' and match[1] == 'Z':
            totalScore += (scissors)
        # Opponent Throws Paper
        elif match[0] == 'B' and match[1] == 'X':
            totalScore += (rock)
        elif match[0] == 'B' and match[1] == 'Y':
            totalScore += (paper + draw)
        elif match[0] == 'B' and match[1] == 'Z':
            totalScore += (scissors + win)
        # Opponent Throws Scissors
        elif match[0] == 'C' and match[1] == 'X':
            totalScore += (rock + win)
        elif match[0] == 'C' and match[1] == 'Y':
            totalScore += (paper)
        elif match[0] == 'C' and match[1] == 'Z':
            totalScore += (scissors + draw)
        else:
            pass
    print(f'Part one answer: {totalScore}')

# X = Lose
# Y = Draw
# Z = Win
def puzzle2(data):
    totalScore = 0
    rock, paper, scissors, draw, win = 1, 2, 3, 3, 6 # Score system
    for i in range(len(data)):
        match = data[i].split()
        if match[1] == 'X': # Calculate Lose
            if match[0] == 'A':
                totalScore += scissors
            elif match[0] == 'B':
                totalScore += rock
            else:
                totalScore += paper
        elif match[1] == 'Y': # Calculate Draw
            if match[0] == 'A':
                totalScore += (draw + rock)
            elif match[0] == 'B':
                totalScore += (draw + paper)
            else:
                totalScore += (draw + scissors)
        else: # Calculate Win
            if match[0] == 'A':
                totalScore += (win + paper)
            elif match[0] == 'B':
                totalScore += (win + scissors)
            else:
                totalScore += (win + rock)
    print(f'Part two answer: {totalScore}')

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