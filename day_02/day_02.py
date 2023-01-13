
def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        out_lines = []
        for line in lines:
            out_lines.append(line.strip())
        return out_lines

def get_rounds():
    rounds = read_file("./input.txt")
    return rounds

def calculate_score(round: str):
    # map record of moves to 0 1 2, where 0 is rock, 1 is paper and 2 is scissors
    opponent_dict = {"A": 0, "B": 1, "C": 2}
    my_dict = {"X": 0, "Y": 1, "Z": 2}

    # shape_score[0] is the score we get for playing rock, etc
    shape_score = [1, 2, 3]

    opp_move = opponent_dict[round[0]]
    my_move = my_dict[round[2]]

    if (opp_move - my_move) % 3 == 0:
        # we drew
        return shape_score[my_move] + 3
    elif (opp_move - my_move) % 3 == 1:
        # we lost
        return shape_score[my_move]
    else:
        # we won!
        return shape_score[my_move] + 6

def calculate_score_part2(round: str):
    # map record of moves to 0 1 2, where 0 is rock, 1 is paper and 2 is scissors
    opponent_dict = {"A": 0, "B": 1, "C": 2}
    strat_dict = {"X": -1, "Y": 0, "Z": 1}
    shape_score = [1, 2, 3]

    opp_move = opponent_dict[round[0]]
    my_strat = strat_dict[round[2]]

    my_move = (opp_move + my_strat) % 3

    if my_strat == -1:
        # we're aiming to lose
        return shape_score[my_move]
    elif my_strat == 0:
        # we're aiming to draw
        return shape_score[my_move] + 3
    else:
        # we're aiming to win
        return shape_score[my_move] + 6


if __name__ == "__main__":
    rounds = get_rounds()
    scores = [calculate_score(round) for round in rounds]
    print(f"Part 1 solution: {sum(scores)}")
    new_scores = [calculate_score_part2(round) for round in rounds]
    print(f"Part 2 solution: {sum(new_scores)}")