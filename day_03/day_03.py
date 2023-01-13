#!/usr/bin/env python3

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        out_lines = []
        for line in lines:
            out_lines.append(line.strip())
        return out_lines

def get_item_priority(item_char):
    ascii_val = ord(item_char)
    if ascii_val > 64:
        if ascii_val > 96:
            # char is lowercase - a-z -> 1-26
            return ascii_val - 96
        else:
            # char is uppercase - A-Z -> 27-52
            return ascii_val - 38
    else:
        raise ValueError(f"Bad char: {item_char}")

def find_common_char(item_list_str: str):
    # bisect the string into two compartments
    com1 = item_list_str[:(len(item_list_str) // 2)]
    com2 = item_list_str[(len(item_list_str) // 2):]
    # find the common char in each
    for char in com1:
        if char in com2:
            return char

def find_common_char_three(str1: str, str2: str, str3: str):
    common_str = str1
    new_common_str = ""
    for char in common_str:
        if char in elf2:
            new_common_str += char
    common_str = new_common_str
    new_common_str = ""
    for char in common_str:
        if char in elf3:
            new_common_str += char
    return new_common_str[0]

if __name__ == "__main__":
    item_lists = read_file("./input.txt")
    result = 0
    for item_list in item_lists:
        common_char = find_common_char(item_list)
        result += get_item_priority(common_char)
    print(f"Part 1 solution: {result}")

    # part 2
    # look at item list in groups of three
    index = 0
    result = 0
    while index < len(item_lists):
        elf1 = item_lists[index]
        elf2 = item_lists[index + 1]
        elf3 = item_lists[index + 2]
        common_char = find_common_char_three(elf1, elf2, elf3)
        result += get_item_priority(common_char)
        index += 3
    print(f"Part 2 solution: {result}")




