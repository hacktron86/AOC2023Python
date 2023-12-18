import re
from functools import reduce


def get_part_number(x, y):
    left, right = [x, y]
    for i in range(x, -1, -1):
        if grid[y][i].isdigit() is True:
            left = i
        else:
            break
    for i in range(x, len(grid[y])):
        if grid[y][i].isdigit() is True:
            right = i
        else:
            break
    part = int("".join(grid[y][left:right + 1]))
    length = len(str(part))
    start = x - left + 1
    return part, length, start


def look_for_parts(x, y):
    parts = []
    for j in range(-1, 2):
        for i in range(-1, 2):
            if grid[y + j][x + i].isdigit() is True:
                part, length, start = get_part_number(x + i, y + j)
                parts.append(part)
                if i + length - start + 1 >= 1:
                    break
    return parts


with open("input.txt", 'r') as f:
    data = [line.strip() for line in f if line.strip()]

grid = [list(line) for line in data]

parts = []

for y, row in enumerate(grid):
    for x, col in enumerate(row):
        matches = re.findall(r'[^.\d]', col)
        for match in matches:
            parts.extend(look_for_parts(x, y))

print(reduce(lambda x, y: x + y, parts))
