import re

f = open('input.txt', 'r')
data = f.read()

# data = '''1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet'''

exceptions = [
        ('oneight', 'oneeight'),
        ('twone', 'twoone'),
        ('threeight', 'threeeight'),
        ('fiveight', 'fiveeight'),
        ('sevenine', 'sevennine'),
        ('eighthree', 'eightthree'),
        ('nineight', 'nineeight'),
        ]

for e in exceptions:
    data = data.replace(e[0], e[1])

data = data.split('\n')

res = 0

for line in data:
    matches = re.findall(r'\d', line)
    res += int(matches[0] + matches[-1])

print(res)
