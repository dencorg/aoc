from aoc_helpers import read_input_from_file

input_str = read_input_from_file('6.txt')

start = 0
# end = 4
end = 14

try:

    while True:
        chars = input_str[start:end]

        if (not chars):
            raise Exception('End of input')

        unique_chars = len(set(chars))

        # if (unique_chars == 4):
        if (unique_chars == 14):
            raise Exception('Marker found')

        start += 1
        end += 1

except Exception as e:
    print(str(e))

    print(end)