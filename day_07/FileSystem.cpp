#include <vector>
#include <stdexcept>

#include "File.h"
#include "FileSystem.h"

FileSystem::FileSystem()
{
    File root{"/"};
    files_.push_back(root);
    cwd = &files_[0];
}

void FileSystem::add_file(std::string name, size_t size = 0)
{
    File new_file{name, size, cwd};
    files_.push_back(new_file);
    if (cwd)
    {
        cwd->add_file(files_.back());
    }
}

void FileSystem::cd(std::string const& dir_name)
{
    if (dir_name == "..")
    {
        // go up to parent
        if (cwd->parent()) cwd = cwd->parent();
    }
    else if (dir_name == ".")
    {
        // do nothing, stay where we are
    }
    else if (dir_name == "/")
    {
        // return to top of filesystem
        cwd = root();
    }
    else
    {
        // look for matching dir in children of cwd
        File* child = cwd->child(dir_name);
        if (!child)
        {
            // tried to access a dir that doesn't exist
            // for now, crash
            std::string err_msg = "Directory " + cwd->path() + " does not contain directory " + dir_name + "\n";
            throw std::runtime_error(err_msg);
        }
    }
}

void FileSystem::ls(std::vector<std::string> const& file_list)
{
    if (file_list.size() )
}

void FileSystem::list_directories() const
{
    for (File const& file : files_)
    {
        if (file.is_dir()) std::cout << file.path() << '\n';
    }
}

size_t FileSystem::sum_dir_sizes_over_size(size_t min_size) const
{
    size_t result = 0;
    for (File const& file : files_)
    {
        if (file.is_dir())
        {
            size_t size = file.size();
            if (size > min_size)
            {
                result += size;
            }
        }
    }
    return result;
}