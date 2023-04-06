from aoc_helpers import read_input_from_file, input_lines

from collections import defaultdict

input_list = input_lines(read_input_from_file('14.txt'))

test_input = [
    '498,4 -> 498,6 -> 496,6',
    '503,4 -> 502,4 -> 502,9 -> 494,9'
]

class SolvePart1:
    def __init__(self, max_size_down, input_list):
        self.max_size_down = max_size_down
        self.start_col = 500
        self.sand_units = 0
        self.input_list = input_list
        self.cave_dict = self.cave_dict_default(max_size_down)

    def cave_dict_default(self, max_size_down):
        return defaultdict(lambda: ["."] * max_size_down)

    def path_add_rock_trace(self, tuple_list):
        for i in range(len(tuple_list) - 1):
            self.add_rock_line(tuple_list[i], tuple_list[i + 1])

    def add_rock_line(self, start, end):
        start_col, start_index = start
        end_col, end_index = end

        if start_col == end_col:
            min_index = min(start_index, end_index)
            max_index = max(start_index, end_index)

            for i in range(min_index, max_index + 1):
                self.cave_dict[start_col][i] = '#'
        else:
            min_col = min(start_col, end_col)
            max_col = max(start_col, end_col)

            for i in range(min_col, max_col + 1):
                self.cave_dict[i][start_index] = '#'

    def sand_move(self, col, down):
        if down == self.max_size_down:
            raise Exception('Reached bottom')

        min_col = min(self.cave_dict.keys())
        max_col = max(self.cave_dict.keys())

        if col == min_col or col == max_col:
            raise Exception('Reached falling borders')

        if self.cave_dict[col][down + 1] == '.':
            return self.sand_move(col, down + 1)
        elif self.cave_dict[col - 1][down + 1] == '.':
            return self.sand_move(col - 1, down + 1)
        elif self.cave_dict[col + 1][down + 1] == '.':
            return self.sand_move(col + 1, down + 1)
        else:
            return col, down

    def print_cave(self):
        if len(self.cave_dict) == 0:
            return 'Empty cave'

        min_col = min(self.cave_dict.keys())
        max_col = max(self.cave_dict.keys())

        output = []
        for i in range(self.max_size_down):
            output.append([])
            for j in range(min_col, max_col + 1):
                output[i].append(self.cave_dict[j][i])

        output.insert(0, list(range(min_col, max_col + 1)))
        toprint = []
        toprint.append(list(range(min_col, max_col + 1)))
        for i in range(1, len(output)):
            toprint.append(''.join(output[i]))

        return toprint

    def populate_cave(self):
        for row in self.input_list:
            row_tuples_list = []
            for i in row.split(" -> "):
                distance_right = int(i.split(",")[0])
                distance_down = int(i.split(",")[1])
                row_tuples_list.append((distance_right, distance_down))

            self.path_add_rock_trace(row_tuples_list)

        self.cave_dict[self.start_col][0] = '+'

    def sand_source_blocked(self):
        return self.cave_dict[self.start_col][0] == 'o'

    def solve(self):
        self.populate_cave()

        while not self.sand_source_blocked():
            try:
                resting_col, resting_down = self.sand_move(self.start_col, 0)
            except Exception as e:
                print('Exception thrown:', e)
                print('Sand units', self.sand_units)
                break

            self.cave_dict[resting_col][resting_down] = 'o'
            self.sand_units += 1

class SolvePart2(SolvePart1):
    def __init__(self, max_size_down, input_list):
        super().__init__(max_size_down, input_list)
        self.max_size_down = max_size_down + 2
        self.cave_dict = self.cave_dict_default(max_size_down + 2)

    def cave_dict_default(self, max_size_down):
        return defaultdict(lambda: ["."] * (max_size_down - 1) + ["#"])

    def sand_move(self, col, down):
        if down == self.max_size_down:
            raise Exception('Reached bottom')

        if self.cave_dict[col][down + 1] == '.':
            return self.sand_move(col, down + 1)
        elif self.cave_dict[col - 1][down + 1] == '.':
            return self.sand_move(col - 1, down + 1)
        elif self.cave_dict[col + 1][down + 1] == '.':
            return self.sand_move(col + 1, down + 1)
        else:
            return col, down

# solver = SolvePart1(10, test_input)
solver = SolvePart1(170, input_list)
solver.solve()
print(solver.sand_units)

# solver2 = SolvePart2(10, test_input)
solver2 = SolvePart2(170, input_list)
solver2.solve()
print(solver2.sand_units)
