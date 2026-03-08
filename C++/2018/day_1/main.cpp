#include <iostream>
#include <fstream>
#include <algorithm>

using std::cout;

int main() {
    
    std::fstream input("./testinput.txt", std::ios_base::in);

    int freq {0};
    int p2_freq {0};
    int i {};

    while (input >> i) {
        freq += i;
    }
    
    cout << "Puzzle 1 - frequency: " << freq << "\n";
    cout << "Puzzle 2 - frequency: " << p2_freq << "\n";

    input.close();
    return 0;
}
