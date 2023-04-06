from aoc_helpers import read_input_from_file, input_lines

from enum import Enum
from functools import cmp_to_key
from copy import deepcopy

input_list = input_lines(read_input_from_file('13.txt'))
# input_list = input_lines(read_input_from_file('13test.txt'))

class Result(Enum):
    RIGHT = 1
    WRONG = -1
    EQUAL = 0

divider_packets = [[[2]], [[6]]]

def get_all_packets_list(input_list):
    packets = []

    for row in input_list:
        if row == '':
            continue
        packets.append(eval(row))

    packets.extend(divider_packets)
    return packets

def get_packets_list(input_list):
    packets = []
    current = ()

    for row in input_list:
        if row == '':
            packets.append(current)
            current = ()
        else:
            current = current + (eval(row),)

    packets.append(current)
    return packets

def compare_lists(left_list, right_list):
    while True:
        left_remaining = len(left_list)
        right_remaining = len(right_list)

        if not left_remaining and not right_remaining:
            return Result.EQUAL

        if (not left_remaining) and right_remaining:
            return Result.RIGHT

        if (not right_remaining) and left_remaining:
            return Result.WRONG

        if left_remaining and right_remaining:
            left_item = left_list.pop(0)
            right_item = right_list.pop(0)

            result = compare(left_item, right_item)
            if result is not Result.EQUAL:
                return result

def compare(left, right):
    # print('comparing', left, right)

    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)

    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)

    if isinstance(left, int) and isinstance(right, list):
        return compare_lists([left], right)

    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right])

    return Result.EQUAL

def compare_ints(left, right):
    if left == right:
        return Result.EQUAL

    if left > right:
        return Result.WRONG
    else:
        return Result.RIGHT

# part 1
packets = get_packets_list(input_list)
order_list = [compare_lists(packet[0], packet[1]) for packet in packets]
# print(order_list)

indices_sum = 0
for idx, result in enumerate(order_list):
    if result is Result.RIGHT:
        indices_sum += idx + 1

print(indices_sum)

# part 2
all_packets = get_all_packets_list(input_list)

def cmp_func(item1, item2):
    result = compare_lists(deepcopy(item1), deepcopy(item2))
    return result.value

sorted_packets = sorted(all_packets, key=cmp_to_key(cmp_func), reverse=True)

dec_key = (sorted_packets.index(divider_packets[0]) + 1) * (sorted_packets.index(divider_packets[1]) + 1)
print(dec_key)
