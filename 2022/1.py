from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('1.txt'))

lists = [[]]

for item in input_list:

    if (item == ''):
        lists.append([])
        continue

    lists_index = len(lists) - 1

    lists[lists_index].append(int(item))


sums = [sum(numbers) for numbers in lists]

print(max(sums))

three_max = sum(sorted(sums)[-3:])

print(three_max)