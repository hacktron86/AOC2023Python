with open('input.txt', 'r') as file:
    directions, map = file.read().strip().split('\n\n')

directions = [x for x in directions.strip()]

map = map.strip().split('\n')

left_dict = {}
right_dict = {}
for line in map:
    key, remainder = line.replace(')', '').split(' = (')
    left, right = remainder.split(', ')
    left_dict[key] = left
    right_dict[key] = right

key = 'AAA'
count = 0
while key != 'ZZZ':
    for d in directions:
        count += 1
        if d == 'R':
            key = right_dict[key]
        if d == 'L':
            key = left_dict[key]
        if key == 'ZZZ':
            break

print(count)
