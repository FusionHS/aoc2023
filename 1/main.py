import solution

with open('input.txt', 'r') as file:
    file_input = file.read()

lines = file_input.split('\n')

solution.get_code(lines, True)
