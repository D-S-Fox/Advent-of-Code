"""

"""
import os.path
from time import perf_counter

def simulate_movement(grid_map, initial_position):
    direction = (0, -1)  # Start facing up (dx, dy)
    x, y = initial_position
    tiles_visited = []

    while True:
        current_position = (x, y)
        next_x = x + direction[0]
        next_y = y + direction[1]

        # Check if out of bounds
        if (y < 0 or y >= len(grid_map) or x < 0 or x >= len(grid_map[0]) or 
            (next_y < 0 or next_y >= len(grid_map) or next_x < 0 or next_x >= len(grid_map[0]))):
            return(len(tiles_visited)+1)
        
        elif grid_map[next_y][next_x] == '#':
            # Change direction: right turn 90 degrees
            if direction == (0, -1):
                direction = (1, 0)
            elif direction == (1, 0):
                direction = (0, 1)
            elif direction == (0, 1):
                direction = (-1, 0)
            elif direction == (-1, 0):
                direction = (0, -1)
            # Update the new position after turning
            x += direction[0]
            y += direction[1]
            if current_position not in tiles_visited:
                tiles_visited.append(current_position)

            #print(f"At - {y}, {x} - Found blocker at - {next_y}, {next_x} - Change direction {direction} - Tile moved {tiles_visited}")
            continue
        else:
            # Move in the current direction
            x += direction[0]
            y += direction[1]
            if current_position not in tiles_visited:
                tiles_visited.append(current_position)
        
def puzzle1(data):
    start_time = perf_counter()
    puzzle1_answer = 0
    
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == '^':
                #print(data[y][x])
                #print(f"{x}, {y}")
                inital_position = (x, y)

    puzzle1_answer = simulate_movement(data, inital_position)

    print(f'Puzzle 1 Answer: {puzzle1_answer}')
    end_time = perf_counter()
    print(f"Puzzle 1 processed in {end_time - start_time:.8f} seconds.\n")

def puzzle2(data):
    start_time = perf_counter()
    puzzle2_answer = 0


    print(f'Puzzle 2 Answer: {puzzle2_answer}')
    end_time = perf_counter()
    print(f"Puzzle 2 processed in {end_time - start_time:.8f} seconds.\n")

def get_input():
    # Gets scripts absolute path and changes to its directory
    start_time = perf_counter()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("input.txt") as infile:
    #with open("testinput.txt") as infile:
        end_time = perf_counter()
        print(f"Got input in {end_time - start_time:.8f} seconds.\n")
        return infile.read().splitlines()
        
def main():
    raw_input=get_input()
    puzzle1(raw_input)
    puzzle2(raw_input)

if __name__ == "__main__":
    main()
