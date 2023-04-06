from aoc_helpers import read_input_from_file, input_lines

from collections import deque
from math import lcm

input_list = input_lines(read_input_from_file('11.txt'))

class Monkey:
    counter = 0

    def __init__(
            self,
            items,
            test_value,
            operation_func = None):
        self.items = deque(items)
        self.test_value = test_value
        self.operation_func = operation_func
        self.monkey_to_throw_if_test_true = None
        self.monkey_to_throw_if_test_false = None
        self.inspections = 0

        self.count = type(self).counter
        type(self).counter += 1

    def __repr__(self):
        return f'Monkey object - Count: {self.count}'

    def has_items(self):
        return len(self.items) > 0

    def set_monkey_to_throw_if_test_true(self, other_monkey):
        self.monkey_to_throw_if_test_true = other_monkey

    def set_monkey_to_throw_if_test_false(self, other_monkey):
        self.monkey_to_throw_if_test_false = other_monkey

    def throw_to(self, other_monkey, item):
        other_monkey.get_item(item)

    def get_item(self, item):
        self.items.append(item)

    def test_func(self, value):
        return value % self.test_value == 0

    def play(self, divide = True, lcm_value = None):
        # inspects an item
        self.inspections += 1

        # get item
        item = self.items.popleft()

        # worry level change by operation function
        item = self.operation_func(item)

        if (divide):
            # worry level is divided by 3
            item = item // 3

        if (lcm_value):
            item = item % lcm_value

        # item is thrown to other monkey, depending of test function outcome item is thrown to other monkey
        if (self.test_func(item)):
            self.throw_to(self.monkey_to_throw_if_test_true, item)
        else:
            self.throw_to(self.monkey_to_throw_if_test_false, item)

monkeys_list = []

# monkeys_list.append(Monkey(
#     [79, 98],
#     23,
#     lambda x: x * 19
# ))

# monkeys_list.append(Monkey(
#     [54, 65, 75, 74],
#     19,
#     lambda x: x + 6
# ))

# monkeys_list.append(Monkey(
#     [79, 60, 97],
#     13,
#     lambda x: x * x
# ))

# monkeys_list.append(Monkey(
#     [74],
#     17,
#     lambda x: x + 3
# ))

# monkeys_list[0].set_monkey_to_throw_if_test_true(monkeys_list[2])
# monkeys_list[0].set_monkey_to_throw_if_test_false(monkeys_list[3])

# monkeys_list[1].set_monkey_to_throw_if_test_true(monkeys_list[2])
# monkeys_list[1].set_monkey_to_throw_if_test_false(monkeys_list[0])

# monkeys_list[2].set_monkey_to_throw_if_test_true(monkeys_list[1])
# monkeys_list[2].set_monkey_to_throw_if_test_false(monkeys_list[3])

# monkeys_list[3].set_monkey_to_throw_if_test_true(monkeys_list[0])
# monkeys_list[3].set_monkey_to_throw_if_test_false(monkeys_list[1])

monkeys_list.append(Monkey(
    [63, 84, 80, 83, 84, 53, 88, 72],
    13,
    lambda x: x * 11
))

monkeys_list.append(Monkey(
    [67, 56, 92, 88, 84],
    11,
    lambda x: x + 4
))

monkeys_list.append(Monkey(
    [52],
    2,
    lambda x: x * x
))

monkeys_list.append(Monkey(
    [59, 53, 60, 92, 69, 72],
    5,
    lambda x: x + 2
))

monkeys_list.append(Monkey(
    [61, 52, 55, 61],
    7,
    lambda x: x + 3
))

monkeys_list.append(Monkey(
    [79, 53],
    3,
    lambda x: x + 1
))

monkeys_list.append(Monkey(
    [59, 86, 67, 95, 92, 77, 91],
    19,
    lambda x: x + 5
))

monkeys_list.append(Monkey(
    [58, 83, 89],
    17,
    lambda x: x * 19
))

monkeys_list[0].set_monkey_to_throw_if_test_true(monkeys_list[4])
monkeys_list[0].set_monkey_to_throw_if_test_false(monkeys_list[7])

monkeys_list[1].set_monkey_to_throw_if_test_true(monkeys_list[5])
monkeys_list[1].set_monkey_to_throw_if_test_false(monkeys_list[3])

monkeys_list[2].set_monkey_to_throw_if_test_true(monkeys_list[3])
monkeys_list[2].set_monkey_to_throw_if_test_false(monkeys_list[1])

monkeys_list[3].set_monkey_to_throw_if_test_true(monkeys_list[5])
monkeys_list[3].set_monkey_to_throw_if_test_false(monkeys_list[6])

monkeys_list[4].set_monkey_to_throw_if_test_true(monkeys_list[7])
monkeys_list[4].set_monkey_to_throw_if_test_false(monkeys_list[2])

monkeys_list[5].set_monkey_to_throw_if_test_true(monkeys_list[0])
monkeys_list[5].set_monkey_to_throw_if_test_false(monkeys_list[6])

monkeys_list[6].set_monkey_to_throw_if_test_true(monkeys_list[4])
monkeys_list[6].set_monkey_to_throw_if_test_false(monkeys_list[0])

monkeys_list[7].set_monkey_to_throw_if_test_true(monkeys_list[2])
monkeys_list[7].set_monkey_to_throw_if_test_false(monkeys_list[1])

# rounds = 20
# rounds = 1000
rounds = 10000

lcm_value = lcm(*[monkey.test_value for monkey in monkeys_list])

for i in range(rounds):
    for m in monkeys_list:
        while m.has_items():
            # m.play()
            m.play(divide=False, lcm_value=lcm_value)

    print('Ending round', i + 1)
    [print(monkey, monkey.items, monkey.inspections) for monkey in monkeys_list]

inspections_list = [monkey.inspections for monkey in monkeys_list]
inspections_list.sort(reverse=True)
monkey_business = inspections_list[0] * inspections_list[1]

print('monkey business', monkey_business)
