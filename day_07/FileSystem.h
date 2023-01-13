#pragma once
#include <vector>
#include <string>
#include <istream>

#include "File.h"

class FileSystem
{
private:
    std::vector<File> files_;
public:
    File* cwd;
    FileSystem();
    void add_file(std::string name, size_t size = 0);

    // commands
    void cd(std::string const& dir_name);
    void ls(std::vector<std::string> const& file_list);
    
    size_t number_of_files() {return files_.size();}

    File* root() { return &files_[0];}

    void list_directories() const;

    size_t sum_dir_sizes_over_size(size_t min_size) const;

};