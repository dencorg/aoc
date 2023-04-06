from aoc_helpers import read_input_from_file, input_lines
import string

letter_list = list(string.ascii_letters)

def get_priority(letter):
    return letter_list.index(letter) + 1

input_list = input_lines(read_input_from_file('3.txt'))

item_priorities = []

for row in input_list:
    first = row[0 : (len(row) // 2)]
    second = row[(len(row) // 2):]

    item_in_both = set(first).intersection(second).pop()

    item_priorities.append(get_priority(item_in_both))

total = sum(item_priorities)
print(total)

group_list = [input_list[i:i+3] for i in range(0, len(input_list), 3)]

new_priorities = [set().union(*group).intersection(*group).pop() for group in group_list]

new_total = sum([get_priority(item) for item in new_priorities])
print(new_total)