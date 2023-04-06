from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('8.txt'))

# right - input_list[idx][idy+1:]
# left - input_list[idx][:idy]
# top - [input_list[i][idy] for i in range(idx)]
# bottom - [input_list[i][idy] for i in range(idx+1, len(input_list))]

def is_visible(x, y):
    height = int(input_list[x][y])

    return is_visible_from_trees(height, trees_from_top(x, y)) or \
        is_visible_from_trees(height, trees_from_bottom(x, y)) or \
        is_visible_from_trees(height, trees_from_left(x, y)) or \
        is_visible_from_trees(height, trees_from_right(x, y))

def get_scenic_score(x, y):
    height = int(input_list[x][y])

    return get_view_distance(height, trees_from_top(x, y)[::-1]) * \
        get_view_distance(height, trees_from_bottom(x, y)) * \
        get_view_distance(height, trees_from_left(x, y)[::-1]) * \
        get_view_distance(height, trees_from_right(x, y))

def get_view_distance(height, other_trees):
    distance = 0

    for other_tree in other_trees:
        if height <= other_tree:
            distance += 1
            break

        distance += 1

    return distance

def trees_from_top(x, y):
    return [int(input_list[i][y]) for i in range(x)]

def trees_from_bottom(x, y):
    return [int(input_list[i][y]) for i in range(x+1, len(input_list))]

def trees_from_left(x, y):
    return [int(i) for i in input_list[x][:y]]

def trees_from_right(x, y):
    return [int(i) for i in input_list[x][y+1:]]

def is_visible_from_trees(height, other_trees):
    return height > max(other_trees)

visible_count = 0
max_score = 0

for idx, row in enumerate(input_list):
    for idy, tree in enumerate(row):
        if idx == 0 or idx == (len(input_list) - 1) or idy == 0 or idy == (len(input_list) - 1):
            continue

        if is_visible(idx, idy):
            visible_count += 1

        # part 2 - tree scenic score
        score = get_scenic_score(idx, idy)
        max_score = max(max_score, score)

edge_visible = (len(input_list[0]) * 2) + (len(input_list) - 2) * 2

total_visible = visible_count + edge_visible
print(total_visible)

print(max_score)
