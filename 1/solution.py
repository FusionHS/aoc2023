import re
from functools import reduce

num_to_digits_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


class CodeInstance:
    def __init__(self, value, index):
        self.value = value
        self.index = index


def convert_to_digits(line):
    digits = []

    numbers = [i for i, c in enumerate(line) if c.isdigit()]
    for index in numbers:
        digits.append(CodeInstance(line[index], index))

    for key, value in num_to_digits_map.items():
        instances = [m.start() for m in re.finditer(key, line)]
        for index in instances:
            digits.append(CodeInstance(value, index))

    digits.sort(key=lambda instance: instance.index)

    return reduce(lambda sum, instance: sum + instance.value, digits, '')


def get_code(lines, convert_digits):
    result = 0

    for line in lines:
        converted = convert_to_digits(line) if convert_digits else line
        code = "".join(re.findall(r'\d+', converted))
        i = int(code[0] + code[-1])
        print('line: ' + line, 'converted: ' + converted, 'code: ' + code, 'code[0]: ' + str(code[0]), 'code[-1]: ' + str(code[-1]), 'i: ' + str(i))
        result += i
    print('Result:', result)
