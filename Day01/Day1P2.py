import re

f = open('input.txt', 'r')
data = f.read()

# data = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''

exceptions = [
        ('oneight', 'oneeight'),
        ('twone', 'twoone'),
        ('threeight', 'threeeight'),
        ('fiveight', 'fiveeight'),
        ('sevenine', 'sevennine'),
        ('eighthree', 'eightthree'),
        ('eightwo', 'eighttwo'),
        ('nineight', 'nineeight'),
        ]

d = {
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

for e in exceptions:
    data = data.replace(e[0], e[1])

data = data.split('\n')

res = 0

for line in data:
    matches = re.findall(
            r'\d|one|two|three|four|five|six|seven|eight|nine', line
            )

    if not matches[0].isdigit():
        matches[0] = d[matches[0]]

    if not matches[-1].isdigit():
        matches[-1] = d[matches[-1]]

    res += int(matches[0] + matches[-1])

print(res)
