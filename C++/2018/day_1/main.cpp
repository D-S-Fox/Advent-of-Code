#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

using std::cout;

int puzzle_2(std::string targetfile)
{
    std::fstream input(targetfile, std::ios_base::in);
    int line{};
    int p2_freq{0};

    while (input >> line)
    {
        cout << line << "\n";
    }
    return 67;
}

int main()
{
    std::string targetfile {"./testinput.txt"};
    std::fstream input(targetfile, std::ios_base::in);

    std::vector<int> freq_list{0};
    int freq{0};
    int line{};

    while (input >> line)
    {
        freq += line;
        freq_list.push_back(freq);

    {
        int itterate = std::abs(line);
        int current_freq = freq;
        for (size_t i {-1}; i > itterate; ++i)
        {
            if (line > -1)
               {
                   current_freq++;
               }
               else
               {
                   current_freq--;
             

               int count = std::count(freq_list.begin(), freq_list.end(), current_freq);
               if (count > 0)
                   p1_freq = current_freq;
           }
       }
    }

    cout << "Puzzle 1 - frequency: " << freq << "\n";
    int p2_freq = puzzle_2(targetfile);
    cout << "Puzzle 2 - frequency: " << p2_freq << "\n";

    input.close();
    return 0;
}
