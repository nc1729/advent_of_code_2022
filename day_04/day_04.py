#!/usr/bin/env python3

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        out_lines = []
        for line in lines:
            out_lines.append(line.strip())
        return out_lines

def overlap(pair):
    a1, b1 = pair[0]
    a2, b2 = pair[1]
    if a2 < a1:
        if b2 < a1:
            return []
        elif b2 == a1:
            return [a1, a1]
        elif a1 < b2 < b1:
            return [a1, b2]
        elif b2 == b1:
            return [a1, b1]
        elif b2 > b1:
            return [a1, b1]
    elif a2 == a1:
        if b2 == a1:
            return [a1, a1]
        elif a1 < b2 < b1:
            return [a1, b2]
        elif b2 == b1:
            return [a1, b1]
        elif b2 > b1:
            return [a1, b1]
    elif a1 < a2 < b1:
        if a1 < b2 < b1:
            return [a2, b2]
        elif b2 == b1:
            return [a2, b1]
        elif b2 > b1:
            return [a2, b1]
    elif a2 == b1:
        if b2 == b1:
            return [a2, b2]
        elif b2 > b1:
            return [a2, a2]
    elif a2 > b1:
        return []

if __name__ == "__main__":
    pair_strings = read_file("./input.txt")
    pairs = []
    for pair_str in pair_strings:
        pair1, pair2 = pair_str.split(",")
        pair1_a, pair1_b = pair1.split("-")
        pair2_a, pair2_b = pair2.split("-")
        pairs.append([[int(pair1_a), int(pair1_b)], [int(pair2_a), int(pair2_b)]])
    
    pairs_with_overlap = 0
    pairs_contain = 0
    for pair in pairs:
        op = overlap(pair)
        if op == pair[0] or op == pair[1]:
            pairs_contain += 1
        if op:
            pairs_with_overlap += 1
    
    print(f"Part 1 solution: {pairs_contain}")
    print(f"Part 2 solution: {pairs_with_overlap}")
    
    