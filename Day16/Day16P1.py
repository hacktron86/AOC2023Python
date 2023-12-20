import sys

def read_file(file_name):
    with open(file_name) as f:
        return f.read().strip().split('\n')


def split_strings(data):
    return [list(line) for line in data]


def continue_forward(prev, cur):
    direction = [a - b for a, b in zip(cur, prev)]
    prev = cur
    new_cur = [a + b for a, b in zip(cur, direction)]
    cur = (new_cur[0], new_cur[1])
    return [prev, cur]


def vertical_split(prev, cur):
    direction = [a - b for a, b in zip(cur, prev)]
    if abs(direction[0]) == 1:
        prev = prev2 = cur
        cur = (prev[0], prev[1] + 1)
        cur2 = (prev2[0], prev2[1] - 1)
        return [prev, cur, prev2, cur2]
    return continue_forward(prev, cur)


def horizontal_split(prev, cur):
    direction = [a - b for a, b in zip(cur, prev)]
    if abs(direction[1]) == 1:
        prev = prev2 = cur
        cur = (prev[0] + 1, prev[1])
        cur2 = (prev2[0] - 1, prev2[1])
        return [prev, cur, prev2, cur2]
    return continue_forward(prev, cur)


def turn_left(prev, cur):
    direction = [a - b for a, b in zip(cur, prev)]
    if abs(direction[0]) == 1:
        prev = cur
        cur = (prev[0], prev[1] - direction[0])
        return [prev, cur]
    if abs(direction[1]) == 1:
        prev = cur
        cur = (prev[0] - direction[1], prev[1])
        return [prev, cur]
    raise ValueError('Direction invalid')


def turn_right(prev, cur):
    direction = [a - b for a, b in zip(cur, prev)]
    if abs(direction[0]) == 1:
        prev = cur
        cur = (prev[0], prev[1] + direction[0])
        return [prev, cur]
    if abs(direction[1]) == 1:
        prev = cur
        cur = (prev[0] + direction[1], prev[1])
        return [prev, cur]
    raise ValueError('Direction invalid')


def check_bounds(data, cur):
    # left
    if cur[1] < 0:
        return False
    # right
    if cur[1] >= len(data):
        return False
    # up
    if cur[0] < 0:
        return False
    if cur[0] >= len(data[0]):
        return False
    return True


def shoot_beam(data, visited, mirrors, splits, prev=(-1, 0), cur=(0, 0)):
    print("New Beam")
    print(len(visited))
    visited.append(cur)
    while True:
        new_coords = []
        split = mirrors[data[cur[1]][cur[0]]](prev, cur)
        if split in splits:
            return visited
        splits.append(split)
        prev, cur, *new_coords = split
        print(prev, cur, *new_coords)
        if new_coords:
            if check_bounds(data, new_coords[1]):
                visited.extend(shoot_beam(data, visited, mirrors, splits, new_coords[0], new_coords[1]))
                visited = list(set(visited))
        if not check_bounds(data, cur):
            print("End Beam")
            return visited
        if cur not in visited:
            visited.append(cur)
        #   if len(visited) > 1000:
        #       print("Over Max")
        #       return visited


def main(data):
    mirrors = {
            '.': continue_forward,
            '|': vertical_split,
            '-': horizontal_split,
            '/': turn_left,
            '\\': turn_right
            }
    visited = []
    splits = []
    return shoot_beam(data, visited, mirrors, splits)

sys.setrecursionlimit(1000)
data = split_strings(read_file('input.txt'))
visited = main(data)
unique_visited = list(set(visited))
print(len(unique_visited))
