import os.path
from time import perf_counter


def puzzle1(data):
    start_time = perf_counter()
    puzzle1_answer = 0

    for ids in data:
        total_id_range = ids.split("-")
        id_1 = int(total_id_range[0])
        id_2 = int(total_id_range[1])

        for i in range(id_2 - id_1 + 1):
            current_id = str(id_1 + i)

            if len(current_id) % 2 == 0:
                midpoint = len(current_id) // 2
                first_half = current_id[:midpoint]
                second_half = current_id[midpoint:]

                if first_half == second_half:
                    puzzle1_answer += int(current_id)

    print(f"Puzzle 1 Answer: {puzzle1_answer}")
    end_time = perf_counter()
    print(f"Puzzle 1 processed in {end_time - start_time:.8f} seconds.\n")


def puzzle2(data):
    start_time = perf_counter()
    puzzle2_answer = 0

    for ids in data:
        total_id_range = ids.split("-")
        id_1 = int(total_id_range[0])
        id_2 = int(total_id_range[1])

        print(f"{id_1} -> {id_2}")
        for id in range(id_2 - id_1 + 1):
            current_id = str(id_1 + id)
            print(f"  {current_id}")


    print(f"Puzzle 2 Answer: {puzzle2_answer}")
    end_time = perf_counter()
    print(f"Puzzle 2 processed in {end_time - start_time:.8f} seconds.\n")


def get_input():
    # Gets scripts absolute path and changes to its directory
    start_time = perf_counter()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    #with open("input.txt") as infile:
    with open("testinput.txt") as infile:
        end_time = perf_counter()
        print(f"Got input in {end_time - start_time:.8f} seconds.\n")
        return infile.read()


def format_data(raw_input):
    start_time = perf_counter()

    data = str(raw_input).split(",")

    end_time = perf_counter()
    print(f"Formated data in {end_time - start_time:.8f} seconds.\n")
    return data


def main():
    raw_input = get_input()
    # print(raw_input)
    data = format_data(raw_input)
    # print(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
