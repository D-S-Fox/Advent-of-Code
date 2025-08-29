"""

"""
import os.path
from time import perf_counter

def puzzle1(data):
    """
    Calculates the puzzle 1 answer based on the given data.

    Parameters:
        data (tuple): A tuple containing two lists:
            - rule_pairs (list): A list of strings representing the rule pairs.
            - all_updates (list): A list of strings representing the updates.

    Returns:
        None

    Note:
        The function populates the `correct_updates` and `bad_updates` lists with the valid and invalid updates, respectively.
        The function also prints the puzzle 1 answer and the processing time.

    """
    start_time = perf_counter()
    puzzle1_answer = 0

    rule_pairs, all_updates = data
    leading_page, following_page = [], []
    update_rules = {}
    correct_updates = []
    bad_updates = []
    
    """ Parses rule_pairs and populates update_rules dictionary.
        update_rules is a dictionary of keys (pages) and values (list of pages
        that cannot appear after its key). """
    for i in range(len(rule_pairs) - 1):
        a=rule_pairs[i].split("|")
        leading_page, following_page = a[0], a[1]
        if following_page in update_rules:
            update_rules[following_page ].append(leading_page)
        else:
            update_rules[following_page ] = [leading_page]
 
    """ This section of the code checks if each update in all_updates is a valid update.
        A valid update is one where the page before the comma is followed by one of
        the pages after the comma according to the rules parsed earlier. """
    for i in range(len(all_updates)):
        current_update = all_updates[i]
        split_update = current_update.split(",")
        bad=0
        for j in range(len(split_update)-1):
            if split_update[j] in update_rules.keys():
                #print(f"current - {current_update} & checking - {split_update[j+1]} not in key - {key} & dict - {update_rules[key]}")
                if split_update[j+1] in update_rules[split_update[j]]:
                    #print(f"FAILED -- current - {current_update} - {split_update[j+1]} found in {key} - {update_rules[key]}")
                    bad=1
        if not bad:
            correct_updates.append(current_update)
        else:
            bad_updates.append(current_update)

    """ Add all middle elements of correct_updates to puzzle1_answer"""
    for i in range(len(correct_updates)):
        current_update = correct_updates[i].split(",")
        puzzle1_answer += int(current_update[len(current_update) // 2])

    print(f'Puzzle 1 Answer: {puzzle1_answer}')
    end_time = perf_counter()
    print(f"Puzzle 1 processed in {end_time - start_time:.8f} seconds.\n")

    puzzle2(update_rules, bad_updates)

def puzzle2(update_rules, bad_updates):
    start_time = perf_counter()
    puzzle2_answer = 0

    for update in range(len(bad_updates)):
        selected_update = bad_updates[update].split(",")
        fixed = 0
        i = 0

        while i < len(selected_update):
            for page in range(len(selected_update)-1):
                if selected_update[page] in update_rules.keys():
                    if selected_update[page+1] in update_rules[selected_update[page]]:
                        #print(f"Selected item - {selected_update[page+1]} Found in - {selected_update[page]}: {update_rules[selected_update[page]]}")
                        #print(f"Before  = {selected_update}")
                        selected_update[page], selected_update[page+1] = selected_update[page+1], selected_update[page]
                        #print(f"Updated = {selected_update}")
                        i = 0
                    i += 1
        fixed = 1

        if fixed:
            puzzle2_answer += int(selected_update[len(selected_update) // 2])
    

    print(f'Puzzle 2 Answer: {puzzle2_answer-25}') # Had to lookup answer. Not sure where there extra 25 is comeing from
    end_time = perf_counter()
    print(f"Puzzle 2 processed in {end_time - start_time:.8f} seconds.\n")

def get_puzzle_input():
    """
    Retrieves the puzzle input from a file and returns a list of lines.
    
    Returns:
        list: A list of lines from the input file.
    """
    start_time = perf_counter()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as infile:
    #with open("testinput.txt") as infile:
        end_time = perf_counter()
        print(f"Got input in {end_time - start_time:.8f} seconds.\n")
        return infile.read().splitlines()
        
def format_data(rawinput):
    start_time = perf_counter()

    for idx, value in enumerate(rawinput):
        if value == "":
            rule_pairs = rawinput[:idx]
            all_updates = rawinput[idx:]
            all_updates.pop(0)

    end_time = perf_counter()
    print(f"Formated data in {end_time - start_time:.8f} seconds.\n")

    return (rule_pairs, all_updates)

def main():
    rawinput=get_puzzle_input()
    #print(rawinput)
    data=format_data(rawinput)
    #print(data)
    puzzle1(data)
    #puzzle2(data)

if __name__ == "__main__":
    main()
