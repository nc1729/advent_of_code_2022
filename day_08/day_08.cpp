#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>

class Map
{
private:
    std::vector<int64_t> trees_;
public:
    Map() = delete;
    Map(std::string const& map_filename);
    int64_t& operator()(int64_t row, int64_t col);
    int64_t const& operator()(int64_t row, int64_t col) const;
    void print_map() const;

    int64_t row_length{0};
    int64_t col_length{0};
};

Map::Map(std::string const& map_filename)
{
    std::ifstream map_file{map_filename};
    std::vector<std::string> map_strings;
    std::string temp;
    while (map_file && std::getline(map_file, temp))
    {
        map_strings.push_back(temp);
    }

    this->row_length = map_strings[0].length();
    this->col_length = map_strings.size();
    this->trees_.reserve(this->row_length * this->col_length);

    for (auto const& map_string : map_strings)
    {
        for (int64_t i = 0; i < map_string.length(); i++)
        {
            int64_t val = static_cast<int64_t>(map_string[i] - '0');
            this->trees_.push_back(val);
        }
    }
}

int64_t& Map::operator()(int64_t row, int64_t col)
{
    return this->trees_[this->row_length * row + col];
}

int64_t const& Map::operator()(int64_t row, int64_t col) const
{
    return this->trees_[this->row_length * row + col];
}

void Map::print_map() const
{
    for (int64_t i = 0; i < row_length; i++)
    {
        for (int64_t j = 0; j < col_length; j++)
        {
            std::cout << (*this)(i, j);
        }
        std::cout << '\n';
    }
    std::cout << '\n';
}

bool tree_is_visible(Map const& tree_map, int64_t row, int64_t col)
{
    // if tree is on the edge of the map, it's visible
    if (row == 0 || row == tree_map.row_length - 1 || col == 0 || col == tree_map.col_length - 1)
    {
        return true;
    }

    // look in all four cardinal directions
    int64_t this_tree = tree_map(row, col);

    // west
    bool visible_from_west = true;
    for (int64_t j = 0; j < col; j++)
    {
        if (tree_map(row, j) >= this_tree)
        {
            // found a taller tree
            visible_from_west = false;
            break;
        }
    }
    if (visible_from_west) return true;

    // east
    bool visible_from_east = true;
    for (int64_t j = col + 1; j < tree_map.col_length; j++)
    {
        if (tree_map(row, j) >= this_tree)
        {
            visible_from_east = false;
            break;
        }
    }
    if (visible_from_east) return true;

    // north
    bool visible_from_north = true;
    for (int64_t i = 0; i < row; i++)
    {
        if (tree_map(i, col) >= this_tree)
        {
            visible_from_north = false;
            break;
        }
    }
    if (visible_from_north) return true;

    // south
    bool visible_from_south = true;
    for (int64_t i = row + 1; i < tree_map.row_length; i++)
    {
        if (tree_map(i, col) >= this_tree)
        {
            visible_from_south = false;
            break;
        }
    }
    if (visible_from_south) return true;

    return false;
}

int64_t count_visible_trees(Map const& tree_map)
{
    int64_t count = 0;
    for (int64_t i = 0; i < tree_map.row_length; i++)
    {
        for (int64_t j = 0; j < tree_map.col_length; j++)
        {
            if (tree_is_visible(tree_map, i, j))
            {
                count++;
            }
        }
    }
    return count;
}

int64_t compute_tree_scenic_score(Map const& tree_map, int64_t row, int64_t col)
{
    // find number of visible trees in all directions
    // there's definitely a smarter way of doing this, but let's just do brute force
    int64_t this_tree = tree_map(row, col);

    // go west
    int64_t visible_trees_west = 0;
    for (int64_t j = 1; j <= col; j++)
    {
        visible_trees_west++;
        if (tree_map(row, col - j) >= this_tree)
        {
            // found a taller tree
            break;
        }
    }

    // east
    int64_t visible_trees_east = 0;
    for (int64_t j = col + 1; j < tree_map.col_length; j++)
    {
        visible_trees_east++;
        if (tree_map(row, j) >= this_tree)
        {
            // found a taller tree
            break;
        }
    }

    // north
    int64_t visible_trees_north = 0;
    for (int64_t i = 1; i <= row; i++)
    {
        visible_trees_north++;
        if (tree_map(row - i, col) >= this_tree)
        {
            break;
        }
    }

    // south
    int64_t visible_trees_south = 0;
    for (int64_t i = row + 1; i < tree_map.row_length; i++)
    {
        visible_trees_south++;
        if (tree_map(i, col) >= this_tree)
        {
            break;
        }
    }

    int64_t scenic_score = visible_trees_west * visible_trees_east * visible_trees_north * visible_trees_south;
    return scenic_score;
}

int64_t find_max_scenic_score(Map const& tree_map)
{
    int64_t max_scenic_score = 0;
    for (int64_t i = 0; i < tree_map.row_length; i++)
    {
        for (int64_t j = 0; j < tree_map.col_length; j++)
        {
            int64_t scenic_score = compute_tree_scenic_score(tree_map, i, j);
            if (scenic_score > max_scenic_score)
            {
                max_scenic_score = scenic_score;
            }
        }
    }

    return max_scenic_score;
}

int main()
{
    Map tree_map{"./input.txt"};
    std::cout << "Row length: " << tree_map.row_length << '\n';
    std::cout << "Col length: " << tree_map.col_length << '\n';
    std::cout << "Number of visible trees: " << count_visible_trees(tree_map) << '\n';
    std::cout << "Max scenic score: " << find_max_scenic_score(tree_map) << '\n';
    return 0;
}