from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('4.txt'))

pair_fully_contains_other = []

partially_contains_other = []

for row in input_list:
    pair1, pair2 = row.split(',')

    pair1_r1, pair1_r2 = pair1.split('-')
    range1 = list(range(int(pair1_r1), int(pair1_r2) + 1))

    pair2_r1, pair2_r2 = pair2.split('-')
    range2 = list(range(int(pair2_r1), int(pair2_r2) + 1))

    # work with strings and substrings
    # range1_str = ''.join(['.'+str(i)+'.' for i in range1])
    # range2_str = ''.join(['.'+str(i)+'.' for i in range2])
    # fully_contains = (range1_str in range2_str) or (range2_str in range1_str)

    # work with sets
    set_range1 = set(range1)
    set_range2 = set(range2)
    fully_contains = (set_range1.issubset(set_range2)) or (set_range2.issubset(set_range1))

    pair_fully_contains_other.append(fully_contains)
    # print(row, fully_contains)

    partially_contains = set_range1.intersection(set_range2)

    partially_contains_other.append(len(partially_contains) > 0)
    # print(row, partially_contains)


# row = "8-8,9-43"

total = pair_fully_contains_other.count(True)
print(total)

total_partial = partially_contains_other.count(True)
print(total_partial)
