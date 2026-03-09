#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <typeinfo>

using std::cout;

int main() {
    
    std::fstream input("./testinput.txt", std::ios_base::in);

    std::vector<int> freq_list {0};
    int freq {0};
    int p2_freq {0};
    int line {};

    while (input >> line) {
        freq += line;
        if (p2_freq == 0 || freq_list.size() >= 1)
        {
            std::string stg {std::to_string(line)};
            if (stg.substr(0, 1) == "-")
            {
                int to_move = std::stoi(stg.substr(1, -1));
                
            }
        }
        freq_list.push_back(freq);
    }
    
    cout << "Puzzle 1 - frequency: " << freq << "\n";
    cout << "Puzzle 2 - frequency: " << p2_freq << "\n";

    input.close();
    return 0;
}
