import math

with open('input.txt', 'r') as file:
    directions, map = file.read().strip().split('\n\n')

directions = [x for x in directions.strip()]

map = map.strip().split('\n')

left_dict = {}
right_dict = {}
keys = []
for line in map:
    key, remainder = (line.replace(')', '').split(' = ('))
    if key.endswith('A'):
        keys.append(key)
    left, right = remainder.split(', ')
    left_dict[key] = left
    right_dict[key] = right

counts = []
for key in keys:
    count = 0
    found = False
    while not found:
        for d in directions:
            count += 1
            if d == 'R':
                key = right_dict[key]
            if d == 'L':
                key = left_dict[key]
            if key.endswith('Z'):
                found = True
    counts += [count]

result = math.lcm(*counts)

print(result)
