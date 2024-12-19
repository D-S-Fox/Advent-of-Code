stack1 = ['T', 'D', 'W', 'Z', 'V', 'P']
stack2 = ['L', 'S', 'W', 'V', 'F', 'J', 'D']
stack3 = ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H']
stack4 = ['R', 'S', 'J']
stack5 = ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W']
stack6 = ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B']
stack7 = ['V', 'J', 'P', 'C', 'B', 'D', 'N']
stack8 = ['P', 'T', 'B', 'Q']
stack9 = ['H', 'G', 'Z', 'R', 'C']

def puzzle1Puller(stack, amount): # Pulls items from given stack and returns items as a list
    pulled = []
    for i in range(int(amount)):
        pulled.append(stack[-1])
        x=stack.pop(-1)
    return pulled

def puzzle1Putter(pulledItems, stackDestination): # Takes stack of items for puzzle1Puller and puts them in the new destination stack
    for i in range(len(pulledItems)):
        stackDestination.append(pulledItems[i])

def puzzle1(data): # ANSWER = TLFGBZHCN
    ANSWER = []
    for i in range(len(data)):
    #for i in range(1):
        # Data/Instruction refinement
        instructions = [] # Index 0=Amount 1=From 2=To
        instSplit = data[i].split() # Splits instructions on spaces
        # Parses data and stores numbers into instruction list
        for j in range(len(instSplit)):
            if instSplit[j].isdigit():
                instructions.append(instSplit[j])
        # WORKING print(instructions)

        # Execute instructions
        amountToPull = instructions[0] # holds amount to remove from top of stack
        if int(instructions[1]) == 1: # From stack one
            transportStack = puzzle1Puller(stack1, amountToPull)
        elif int(instructions[1]) == 2: # From stack two
            transportStack = puzzle1Puller(stack2, amountToPull)
        elif int(instructions[1]) == 3: # From stack three
            transportStack = puzzle1Puller(stack3, amountToPull)
        elif int(instructions[1]) == 4: # From stack four
            transportStack = puzzle1Puller(stack4, amountToPull)
        elif int(instructions[1]) == 5: # From stack five
            transportStack = puzzle1Puller(stack5, amountToPull)
        elif int(instructions[1]) == 6: # From stack six
            transportStack = puzzle1Puller(stack6, amountToPull)
        elif int(instructions[1]) == 7: # From stack seven
            transportStack = puzzle1Puller(stack7, amountToPull)
        elif int(instructions[1]) == 8: # From stack eight
            transportStack = puzzle1Puller(stack8, amountToPull)
        elif int(instructions[1]) == 9: # From stack nine
            transportStack = puzzle1Puller(stack9, amountToPull)

        if int(instructions[2]) == 1: # To stack one
            puzzle1Putter(transportStack, stack1)
        elif int(instructions[2]) == 2: # To stack two
            puzzle1Putter(transportStack, stack2)
        elif int(instructions[2]) == 3: # To stack three
            puzzle1Putter(transportStack, stack3)
        elif int(instructions[2]) == 4: # To stack four
            puzzle1Putter(transportStack, stack4)
        elif int(instructions[2]) == 5: # To stack five
            puzzle1Putter(transportStack, stack5)
        elif int(instructions[2]) == 6: # To stack six
            puzzle1Putter(transportStack, stack6)
        elif int(instructions[2]) == 7: # To stack seven
            puzzle1Putter(transportStack, stack7)
        elif int(instructions[2]) == 8: # To stack eight
            puzzle1Putter(transportStack, stack8)
        elif int(instructions[2]) == 9: # To stack nine
            puzzle1Putter(transportStack, stack9)

    # Find create on top of each stack
    ANSWER.append(stack1[-1])
    ANSWER.append(stack2[-1])
    ANSWER.append(stack3[-1])
    ANSWER.append(stack4[-1])
    ANSWER.append(stack5[-1])
    ANSWER.append(stack6[-1])
    ANSWER.append(stack7[-1])
    ANSWER.append(stack8[-1])
    ANSWER.append(stack9[-1])
    print('Day one answer: ' + ''.join(ANSWER))

def puzzle2Puller(stack, amount): # Pulls items from given stack and returns items as a list
    pulled = []
    for i in range(int(amount)):
        pulled.append(stack[-1])
        stack.pop(-1)
        pulledStack = pulled[::-1] # Reverses list so it's as if all items were pulled off as a stack
    return pulledStack

def puzzle2Putter(pulledItems, stackDestination): # Takes stack of items for puzzle1Puller and puts them in the new destination stack
    for i in range(len(pulledItems)):
        stackDestination.append(pulledItems[i])

def puzzle2(data):
    ANSWER = []
    for i in range(len(data)):
        # Data/Instruction refinement
        instructions = [] # Index 0=Amount 1=From 2=To
        instSplit = data[i].split() # Splits instructions on spaces
        # Parses data and stores numbers into instruction list
        for j in range(len(instSplit)):
            if instSplit[j].isdigit():
                instructions.append(instSplit[j])
        # WORKING print(instructions)

        # Execute instructions
        amountToPull = instructions[0] # holds amount to remove from top of stack
        if int(instructions[1]) == 1: # From stack one
            transportStack = puzzle2Puller(stack1, amountToPull)
        elif int(instructions[1]) == 2: # From stack two
            transportStack = puzzle2Puller(stack2, amountToPull)
        elif int(instructions[1]) == 3: # From stack three
            transportStack = puzzle2Puller(stack3, amountToPull)
        elif int(instructions[1]) == 4: # From stack four
            transportStack = puzzle2Puller(stack4, amountToPull)
        elif int(instructions[1]) == 5: # From stack five
            transportStack = puzzle2Puller(stack5, amountToPull)
        elif int(instructions[1]) == 6: # From stack six
            transportStack = puzzle2Puller(stack6, amountToPull)
        elif int(instructions[1]) == 7: # From stack seven
            transportStack = puzzle2Puller(stack7, amountToPull)
        elif int(instructions[1]) == 8: # From stack eight
            transportStack = puzzle2Puller(stack8, amountToPull)
        elif int(instructions[1]) == 9: # From stack nine
            transportStack = puzzle2Puller(stack9, amountToPull)

        if int(instructions[2]) == 1: # To stack one
            puzzle2Putter(transportStack, stack1)
        elif int(instructions[2]) == 2: # To stack two
            puzzle2Putter(transportStack, stack2)
        elif int(instructions[2]) == 3: # To stack three
            puzzle2Putter(transportStack, stack3)
        elif int(instructions[2]) == 4: # To stack four
            puzzle2Putter(transportStack, stack4)
        elif int(instructions[2]) == 5: # To stack five
            puzzle2Putter(transportStack, stack5)
        elif int(instructions[2]) == 6: # To stack six
            puzzle2Putter(transportStack, stack6)
        elif int(instructions[2]) == 7: # To stack seven
            puzzle2Putter(transportStack, stack7)
        elif int(instructions[2]) == 8: # To stack eight
            puzzle2Putter(transportStack, stack8)
        elif int(instructions[2]) == 9: # To stack nine
            puzzle2Putter(transportStack, stack9)
    # Find create on top of each stack
    ANSWER.append(stack1[-1])
    ANSWER.append(stack2[-1])
    ANSWER.append(stack3[-1])
    ANSWER.append(stack4[-1])
    ANSWER.append(stack5[-1])
    ANSWER.append(stack6[-1])
    ANSWER.append(stack7[-1])
    ANSWER.append(stack8[-1])
    ANSWER.append(stack9[-1])
    print('Day two answer: ' + ''.join(ANSWER))

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
    #puzzle2(rawinput)

if __name__ == "__main__":
    main()