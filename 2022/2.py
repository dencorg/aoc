from aoc_helpers import read_input_from_file, input_lines
from enum import Enum

input_list = input_lines(read_input_from_file('2.txt'))

class Outcome(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

# 1 for Rock, 2 for Paper, and 3 for Scissors) 

shape_score_dict = {'X': 1, 'Y': 2, 'Z': 3}

# Opponent: A for Rock, B for Paper, and C for Scissors
# You: X for Rock, Y for Paper, and Z for Scissors

outcome_dict = {
    'AX': Outcome.DRAW,
    'AY': Outcome.WIN,
    'AZ': Outcome.LOSE,
    'BX': Outcome.LOSE,
    'BY': Outcome.DRAW,
    'BZ': Outcome.WIN,
    'CX': Outcome.WIN,
    'CY': Outcome.LOSE,
    'CZ': Outcome.DRAW,
}

# Part 1

scores = []

for row in input_list:
    outcome = outcome_dict[row.replace(" ", "")]
    scores.append(outcome.value + shape_score_dict[row[2]])

total_score = sum(scores)

print(total_score)

# Part 2

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

class MyShape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Opponent: A for Rock, B for Paper, and C for Scissors

new_outcome_dict = {
    'AX': [Outcome.LOSE, MyShape.SCISSORS],
    'AY': [Outcome.DRAW, MyShape.ROCK],
    'AZ': [Outcome.WIN, MyShape.PAPER],
    'BX': [Outcome.LOSE, MyShape.ROCK],
    'BY': [Outcome.DRAW, MyShape.PAPER],
    'BZ': [Outcome.WIN, MyShape.SCISSORS],
    'CX': [Outcome.LOSE, MyShape.PAPER],
    'CY': [Outcome.DRAW, MyShape.SCISSORS],
    'CZ': [Outcome.WIN, MyShape.ROCK]
}

new_scores = []

for row in input_list:
    outcome = new_outcome_dict[row.replace(" ", "")]
    new_score = outcome[0].value + outcome[1].value
    new_scores.append(new_score)

new_total_score = sum(new_scores)

print(new_total_score)


