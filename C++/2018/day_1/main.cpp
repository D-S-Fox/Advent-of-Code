#include <iostream>
#include <fstream>
#include <string>

int main() {
    
    std::fstream input("./input.txt", std::ios_base::in);

    int freq = 0;
    int num;
    while (input >> num) {
        freq += num;
    }

    printf("Puzzle 1 - frequency: %d\n", freq);
    return 0;
}
