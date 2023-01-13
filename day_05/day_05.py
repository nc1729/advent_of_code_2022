#!/usr/bin/env python3
import copy
from typing import List

def make_stacks(stack_data: str) -> List[str]:
    stack_data_str_array = stack_data.split("\n")
    stack_num_str = stack_data_str_array[-1]
    number_of_stacks = (len(stack_num_str) + 1) // 4
    number_of_cols = len(stack_data_str_array) - 1
    stacks = []
    for i in range(number_of_stacks):
        # construct the ith stack
        new_stack = ""
        for j in range(number_of_cols - 1, -1, -1):
            if stack_data_str_array[j][4*i+1] != " ":
                new_stack += stack_data_str_array[j][4*i+1]
        stacks.append(new_stack)
    return stacks

def make_moves(move_data: str) -> List[List[int]]:
    moves = []
    move_data_str_array = move_data.split("\n")
    for move_data_str in move_data_str_array:
        if move_data_str:
            space_split_array = move_data_str.split()
            moves.append([int(space_split_array[1]), int(space_split_array[3]) - 1, int(space_split_array[5]) - 1])
    return moves

def apply_move_to_stacks(stacks: List[str], move: List[int]):
    # move is [int, int, int] - move[0] is number to move, move[1] is stack to move from, move[2] is stack to move to
    number_to_move = move[0]
    stack_from = stacks[move[1]]
    stack_to = stacks[move[2]]

    stack_from = stack_from[::-1] # reverse stack_from
    moved_crates = stack_from[:number_to_move]
    new_stack_from = stack_from[number_to_move:][::-1] # undo reverse of original stack
    new_stack_to = stack_to + moved_crates

    stacks[move[1]] = new_stack_from
    stacks[move[2]] = new_stack_to

    return stacks

def apply_move_to_stacks_part2(stacks: List[str], move: List[int]):
    # move is [int, int, int] - move[0] is number to move, move[1] is stack to move from, move[2] is stack to move to
    number_to_move = move[0]
    stack_from = stacks[move[1]]
    stack_to = stacks[move[2]]

    moved_crates = stack_from[(len(stack_from) - number_to_move):]
    new_stack_from = stack_from[:(len(stack_from) - number_to_move)]
    new_stack_to = stack_to + moved_crates

    stacks[move[1]] = new_stack_from
    stacks[move[2]] = new_stack_to

    return stacks

if __name__ == "__main__":
    raw_file_data = ""
    with open("./input.txt") as f:
        raw_file_data = f.read()

    stack_data_end = raw_file_data.find("\n\n")
    stack_data = raw_file_data[:stack_data_end]
    move_data = raw_file_data[stack_data_end+2:]

    # first parse stack data
    stacks = make_stacks(stack_data)
    stacks1 = copy.deepcopy(stacks)
    stacks2 = copy.deepcopy(stacks)

    # now parse move data
    moves = make_moves(move_data)

    for move in moves:
        stacks1 = apply_move_to_stacks(stacks1, move)
    
    out_string = ""
    for stack in stacks1:
        out_string += stack[-1]
    
    print(f"Part 1 solution: {out_string}")

    for move in moves:
        stacks2 = apply_move_to_stacks_part2(stacks2, move)
    
    out_string = ""
    for stack in stacks2:
        out_string += stack[-1]
    
    print(f"Part 2 solution: {out_string}")
    