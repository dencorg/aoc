from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('5.txt'))

#     [P]                 [Q]     [T]
# [F] [N]             [P] [L]     [M]
# [H] [T] [H]         [M] [H]     [Z]
# [M] [C] [P]     [Q] [R] [C]     [J]
# [T] [J] [M] [F] [L] [G] [R]     [Q]
# [V] [G] [D] [V] [G] [D] [N] [W] [L]
# [L] [Q] [S] [B] [H] [B] [M] [L] [D]
# [D] [H] [R] [L] [N] [W] [G] [C] [R]
#  1   2   3   4   5   6   7   8   9 

def create_stacks():
    stacks = []
    stacks.append(['D', 'L', 'V', 'T', 'M', 'H', 'F'])
    stacks.append(['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P'])
    stacks.append(['R', 'S', 'D', 'M', 'P', 'H'])
    stacks.append(['L', 'B', 'V', 'F'])
    stacks.append(['N', 'H', 'G', 'L', 'Q'])
    stacks.append(['W', 'B', 'D', 'G', 'R', 'M', 'P'])
    stacks.append(['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q'])
    stacks.append(['C', 'L', 'W'])
    stacks.append(['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T'])
    return stacks

stacks = create_stacks()

for row in input_list:
    if not row.startswith('move'):
        continue

    action = row.split()

    times = int(action[1])
    from_stack = int(action[3])
    to_stack = int(action[5])

    for i in range(times):
        crate = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(crate)

top_crates = [stack[-1] for stack in stacks]
crates_str = ''.join(top_crates)
print(crates_str)

stacks2 = create_stacks()

for row in input_list:
    if not row.startswith('move'):
        continue

    action = row.split()

    times = int(action[1])
    from_stack = int(action[3])
    to_stack = int(action[5])

    take = stacks2[from_stack - 1][-times:]
    stacks2[from_stack - 1] = stacks2[from_stack - 1][:-times]
    stacks2[to_stack - 1].extend(take)


top_crates2 = [stack2[-1] for stack2 in stacks2]
crates_str2 = ''.join(top_crates2)
print(crates_str2)
