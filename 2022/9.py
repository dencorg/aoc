from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('9.txt'))

# 2-1   20  21  22  23  24
# 1-1   10  11  12  13  14
# 0-1   00  01  02  03  04
# -1-1 -10 -11 -12 -13 -14

# go right -> same x, increase y
# go up -> increase x, same y
# go left -> same x, decrease y
# go down -> decrease x, same y

def move_head(move, head_point):
    x, y = head_point

    match move:
        case 'R':
            return (x, y + 1)
        case 'U':
            return (x + 1, y)
        case 'L':
            return (x, y - 1)
        case 'D':
            return (x - 1, y)

def move_tail_after_head(tail_point, head_point):
    if tail_is_touching_head(tail_point, head_point):
        return tail_point

    tail_x, tail_y = tail_point
    head_x, head_y = head_point

    # move on same row x
    if head_x == tail_x:
        if head_y > tail_y:
            return (tail_x, head_y - 1)
        else:
            return (tail_x, head_y + 1)

    # move on same column y
    if head_y == tail_y:
        if head_x > tail_x:
            return (head_x - 1, tail_y)
        else:
            return (head_x + 1, tail_y)

    # move diagonally
    possible_points = tail_possible_diag_moves(tail_point)
    for point in possible_points:
        if tail_is_touching_head(point, head_point):
            return point

def tail_is_touching_head(tail, head):
    return (abs(tail[0] - head[0]) < 2) and (abs(tail[1] - head[1]) < 2)

def tail_possible_diag_moves(tail_point):
    x, y = tail_point
    return (
        (x + 1, y + 1), # diag up right
        (x - 1, y + 1), # diag down right
        (x - 1, y - 1), # diag down left
        (x + 1, y - 1 ), # diag up left
    )

# part 1
# starting point
head = (0, 0)
tail = (0, 0)

tail_moves_set = set()
tail_moves_set.add(tail)

# part 2
knot_h = (0, 0)
knot_1 = (0, 0)
knot_2 = (0, 0)
knot_3 = (0, 0)
knot_4 = (0, 0)
knot_5 = (0, 0)
knot_6 = (0, 0)
knot_7 = (0, 0)
knot_8 = (0, 0)
knot_t = (0, 0)

knot_t_moves = set()
knot_t_moves.add(knot_t)

for row in input_list:
    move, times = row.split()

    for i in range(int(times)):
        # part 1
        head = move_head(move, head)
        # print('HEAD:', head)

        tail = move_tail_after_head(tail, head)
        # print('TAIL:', tail)

        tail_moves_set.add(tail)

        # part 2
        knot_h = move_head(move, knot_h)

        knot_1 = move_tail_after_head(knot_1, knot_h)
        knot_2 = move_tail_after_head(knot_2, knot_1)
        knot_3 = move_tail_after_head(knot_3, knot_2)
        knot_4 = move_tail_after_head(knot_4, knot_3)
        knot_5 = move_tail_after_head(knot_5, knot_4)
        knot_6 = move_tail_after_head(knot_6, knot_5)
        knot_7 = move_tail_after_head(knot_7, knot_6)
        knot_8 = move_tail_after_head(knot_8, knot_7)
        knot_t = move_tail_after_head(knot_t, knot_8)

        # print('TAIL9:', knot_t)

        knot_t_moves.add(knot_t)

print('TAIL 1 moves: ', len(tail_moves_set))

print('TAIL 9 moves: ', len(knot_t_moves))
