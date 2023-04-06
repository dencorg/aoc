from aoc_helpers import read_input_from_file, input_lines

from string import ascii_lowercase

input_list = input_lines(read_input_from_file('12.txt'))

def can_move_to(current_mark, point):
    x, y = point
    other_mark = input_list[x][y]

    if (current_mark == 'z'):
        next_elevation = 'z'
    else:
        next_elevation = ascii_lowercase[ascii_lowercase.find(current_mark) + 1]

    return (current_mark == other_mark) or (other_mark == next_elevation) or \
        (ascii_lowercase.find(other_mark) < ascii_lowercase.find(current_mark))

def get_neighbours(x, y):
    mark = input_list[x][y]

    if mark == 'S':
        mark = 'a'

    if mark == 'E':
        mark = 'z'

    x_size = len(input_list)
    y_size = len(input_list[0])

    possible_positions = list(
        filter(
            lambda arg: (arg[0] >= 0 and arg[0] < x_size) and (arg[1] >= 0 and arg[1] < y_size), 
            [
                (x, y + 1), # right >
                (x + 1, y), # down v
                (x, y - 1), # left <
                (x - 1, y) # up ^
            ]
        )
    )

    return [position for position in possible_positions if can_move_to(mark, position)]

def create_adj_list():
    adj_list = {}
    start_point = None
    end_point = None

    for idx, row in enumerate(input_list):
        for idy, elevation in enumerate(row):
            adj_list[(idx, idy)] = get_neighbours(idx, idy)

            if elevation == 'S':
                start_point = (idx, idy)

            if elevation == 'E':
                end_point = (idx, idy)

    return (start_point, end_point, adj_list)

def bfs_with_depth(graph, source_node, end_node):
    visited = set()
    queue = []

    queue.append((source_node, 0))
    visited.add(source_node)

    while queue:
        current_node, depth = queue.pop(0)

        if (current_node == end_node):
            return depth

        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append((neighbour_node, depth + 1))


# part 1
start_point, end_point, adj_list = create_adj_list()
steps = bfs_with_depth(adj_list, start_point, end_point)
print(steps)

# part 2
a_marks_list = []

for idx, row in enumerate(input_list):
    for idy, elevation in enumerate(row):
        if elevation == 'a' or elevation == 'S':
            a_marks_list.append((idx, idy))

all_steps_dict = {}

for m in a_marks_list:
    a_depth = bfs_with_depth(adj_list, m, end_point)
    if (a_depth is not None):
        all_steps_dict[m] = a_depth

min_steps = min(all_steps_dict.values())
print(min_steps)
