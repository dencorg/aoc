from collections import defaultdict
from pathlib import PurePath

from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('7.txt'))

current_path = None
dir_dict = defaultdict(int)
files_dict = {}

for row in input_list:
    parts = row.split()

    match parts[0]:
        case '$':
            cmd_name = parts[1]

            match cmd_name:
                case 'cd':
                    name = parts[2]

                    if name == '..':
                        current_path = current_path.parent

                    else:
                        if current_path is None:
                            current_path = PurePath(name)
                        else:
                            current_path = current_path / name

                    # print('cd ' + str(current_path))

                case 'ls':
                    pass

        case 'dir':
            dir_name = parts[1]
            dir_path = current_path / dir_name
            # print('dir ' + dir_name + ' in ' + str(current_path))

        case _:
            file_name = parts[1]
            file_size = int(parts[0])
            # print('file ' + file_name + ' in ' + str(current_path) + ' - size: ' + str(file_size))

            file_path = current_path / file_name

            files_dict[file_path] = file_size

            for path in file_path.parents:
                dir_dict[path] += file_size


filtered_dict = {path: size for path, size in dir_dict.items() if size <= 100000}

total_sum = sum(filtered_dict.values())
print(total_sum)

total_available_space = 70000000
needs_unused_space = 30000000

used_space = max(dir_dict.values())
current_unused_space = total_available_space - used_space

available_sizes_dict = {purepath: dirsize for purepath, dirsize in dir_dict.items() if current_unused_space + dirsize >= needs_unused_space}

min_size_dir = min(available_sizes_dict.values())
print(min_size_dir)
