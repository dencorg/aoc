from aoc_helpers import read_input_from_file, input_lines

input_list = input_lines(read_input_from_file('10.txt'))

# 20th, 60th, 100th, 140th, 180th, and 220th cycles
cycles_check_at = [20, 60, 100, 140, 180, 220]
signal_strengths = []

def check_cycle(counter, reg_value):
    if counter in cycles_check_at:
        signal_strength = counter * reg_value
        signal_strengths.append(signal_strength)

def crt_draw(position, reg_value):
    if position in spite_position(reg_value):
        return '#'
    else:
        return '.'

def spite_position(reg_value):
    return (reg_value - 1, reg_value, reg_value + 1)

X = 1
cycles_counter = 0

crt_output = []

for row in input_list:

    print('***', row)

    parts = row.split()
    instruction = parts[0]

    match instruction:
        case 'noop':
            cycles_counter += 1

            check_cycle(cycles_counter, X)

            position = (cycles_counter - 1) % 40
            crt_output.append(crt_draw(position, X))

            print(f"During: {cycles_counter}. X is {X}.")
            print(f"Crt position is: {position}")

        case 'addx':
            number = int(parts[1])

            cycles_counter += 1

            check_cycle(cycles_counter, X)

            position = (cycles_counter - 1) % 40
            crt_output.append(crt_draw(position, X))

            print(f"During cycle: {cycles_counter}. X is {X}.")
            print(f"Crt position is: {position}")

            cycles_counter += 1

            check_cycle(cycles_counter, X)

            position = (cycles_counter - 1) % 40
            crt_output.append(crt_draw(position, X))

            print(f"During cycle: {cycles_counter}. X is {X}.")
            print(f"Crt position is: {position}")

            X += number

signal_sum = sum(signal_strengths)
print(signal_sum)

print(''.join(crt_output[0:40]))
print(''.join(crt_output[40:80]))
print(''.join(crt_output[80:120]))
print(''.join(crt_output[120:160]))
print(''.join(crt_output[160:200]))
print(''.join(crt_output[200:240]))

# RFKZCPEF
