#include <vector>
#include <string>

#include "File.h"

size_t File::size() const
{
    size_t result = 0;
    if (this->is_dir())
    {
        // walk the children of this file and compute the file size of each
        // could cache for performance...
        for (File const* file : children_)
        {
            result += file->size();
        }
    }
    else
    {
        result = size_;
    }
    return result;
}

std::string File::path() const
{
    if (name_ == "/")
    {
        return name_;
    }
    else
    {
        std::string out;
        return this->parent_->path() + "/" + name_;
    }
}

void File::add_file(File& new_file)
{
    children_.push_back(&new_file);
}

File* File::child(std::string const& name)
{
    for (File* child : children_)
    {
        if (child->name() == name)
        {
            return child;
        }
    }
    return nullptr;
}