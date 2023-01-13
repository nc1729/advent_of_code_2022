#!/usr/bin/python3
import sys

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        out_lines = []
        for line in lines:
            out_lines.append(line.strip())
        return out_lines

if __name__ == "__main__":
    # read file
    if len(sys.argv) < 2:
        print("Usage ./day_01.py [FILENAME]")
    lines = read_file(sys.argv[1])

    # compute sums of line separated entries
    sums = []
    sum = 0
    for line in lines:
        if len(line) == 0:
            sums.append(sum)
            sum = 0
        else:
            sum += int(line)
    sums.sort()

    # get max value
    print(f"Part 1 solution: {sums[-1]}")

    # get max three values
    max_three = sums[-1] + sums[-2] + sums[-3]
    print(f"Part 2 solution: {max_three}")
