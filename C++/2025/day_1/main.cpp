#include <iostream>
#include <string>
#include <fstream>

using std::cout, std::string;

int main()
{
    string targetfile{"testinput.txt"};

    std::ifstream f(targetfile);
    if (!f)
    {
        cout << "Failed to open file: " << targetfile << "\n";
        return 1;
    }

    string line{};
    while (std::getline(f, line))
    {
        cout << line << "\n";
    }

    return 0;
}