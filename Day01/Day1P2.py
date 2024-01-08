import re

ex =    {
            'oneight': 'oneeight',
            'twone': 'twoone',
            'threeight': 'threeeight',
            'fiveight': 'fiveeight',
            'sevenine': 'sevennine',
            'eightwo': 'eighttwo',
            'eighthree': 'eightthree',
            'nineight': 'nineeight'
        }

d =     {
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

data = open(0).read().strip()

for key, value in ex.items():
    data = data.replace(key, value)

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
