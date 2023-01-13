#include <iostream>
#include <fstream>
#include <stdexcept>

#include "File.h"
#include "FileSystem.h"

int main()
{
    // let's set aside somewhere to put our files
    FileSystem filesystem;

    // open a filestream
    std::ifstream input_file{"./test.txt"};
    std::vector<std::string> input;
    std::string word;
    while (input_file >> word)
    {
        input.push_back(word);
    }

    size_t index = 0;
    while (index < input.size())
    {
        if (input[index] == "$")
        {
            // found a command
            parse_command(input, filesystem, index);
        }
    }

    // get sizes of directories
    filesystem.list_directories();

    filesystem.sum_directory_sizes_over_100k();


}