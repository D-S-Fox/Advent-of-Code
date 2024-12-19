def puzzle1(data):
    elfNum = 0
    calories = 0
    caloriePerElf = []
    # Count calories per elf
    for i in range(len(data)):
        if str(data[i]).isdigit():
            calories += int(data[i])
        else:
            elfNum += 1
            caloriePerElf.append(calories)
            calories -= calories

    #Finds which elf has the most calories
    elfCarryingAmount = max(caloriePerElf)
    elfCarryingMost = caloriePerElf.index(elfCarryingAmount)
    print(f'Elf {elfCarryingMost} is carrying {elfCarryingAmount} calories.')

def puzzle2(data):
    elfNum = 0
    calories = 0
    caloriePerElf = []
    # Count calories per elf
    for i in range(len(data)):
        if str(data[i]).isdigit():
            calories += int(data[i])
        else:
            elfNum += 1
            caloriePerElf.append(calories)
            calories -= calories

    #Finds total calories of top three elves
    caloriePerElf.sort()
    total = caloriePerElf[-1] + caloriePerElf[-2] + caloriePerElf[-3]
    print(f'The total calories for the top three elves is {total}.')


def getinput():
    array = []
    with open("input.txt") as infile:
        for line in infile:
            line = line.strip('\n')
            array.append(line)
        return array

def main():
    rawinput = getinput()
    #print(rawinput[12:15])
    puzzle1(rawinput)
    puzzle2(rawinput)

if __name__ == "__main__":
    main()