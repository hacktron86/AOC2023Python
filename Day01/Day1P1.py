import re

ex =    {
            'oneight': 'oneeight',
            'twone': 'twoone',
            'threeight': 'threeeight',
            'fiveight': 'fiveeight',
            'sevenine': 'sevennine',
            'eighthree': 'eightthree',
            'nineight': 'nineeight'
        }

data = open(0).read().strip()

for key, value in ex.items():
    data = data.replace(key, value)

data = data.split('\n')

res = 0

for line in data:
    matches = re.findall(r'\d', line)
    res += int(matches[0] + matches[-1])

print(res)
