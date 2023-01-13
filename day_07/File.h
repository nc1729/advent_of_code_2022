#pragma once
#include <iostream>
#include <vector>
#include <string>

/*
File - a class to model a node in a filesystem tree.
*/
class File
{
private:
    std::vector<File*> children_;
    // store a pointer to the parent directory (nullptr is this file is "/")
    File* parent_;
    size_t size_;
    std::string name_;
public:
    File() = delete;
    File(std::string const& name, size_t size = 0, File* parent = nullptr) :
        name_{name}, size_{size}, parent_{parent} {};
    
    // calculate size of file (== size_ if contents_ is empty, otherwise recursively calculates)
    size_t size() const;

    std::string name() const {return name_;}

    // walk up the filesystem to generate this file's full path
    std::string path() const;

    // a file is a directory if it contains pointers to other files
    bool is_dir() const {return children_.size() > 0;}

    void add_file(File& new_file);

    File* parent() { return parent_; }

    // find a child file using its name
    File* child(std::string const& name);
};