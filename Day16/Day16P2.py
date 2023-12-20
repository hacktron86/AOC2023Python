import sys
import multiprocessing

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
    #print("New Beam")
    #print(len(visited))
    visited.append(cur)
    while True:
        new_coords = []
    #    print("Coords:", cur, "Mirror:", data[cur[1]][cur[0]])
        split = mirrors[data[cur[1]][cur[0]]](prev, cur)
        if split in splits:
            return list(set(visited))
        splits.append(split)
        prev, cur, *new_coords = split
    #    print(prev, cur, *new_coords)
        if new_coords:
            if check_bounds(data, new_coords[1]):
                visited.extend(shoot_beam(data, visited, mirrors, splits, new_coords[0], new_coords[1]))
                visited = list(set(visited))
        if not check_bounds(data, cur):
    #        print("End Beam")
            return list(set(visited))
        if cur not in visited:
            visited.append(cur)


def create_edge_pairs(width, height):
    edge_pairs = []

    for x in range(width):
        edge_pairs.append(((-1, x), (0, x)))
        edge_pairs.append(((height, x), (height - 1, x)))

    for y in range(1, height):
        edge_pairs.append(((y, -1), (y, 0)))
        edge_pairs.append(((y, width), (y, width - 1)))

    return edge_pairs


def process_coord(data, mirrors, coord):
    visited = []
    splits = []
    return shoot_beam(data, visited, mirrors, splits, coord[0], coord[1])


def main(data):
    mirrors = {
            '.': continue_forward,
            '|': vertical_split,
            '-': horizontal_split,
            '/': turn_left,
            '\\': turn_right
            }
    starting_coords = create_edge_pairs(len(data[0]), len(data))

    with multiprocessing.Pool() as pool:
        results = pool.starmap(process_coord, [(data, mirrors, coord) for coord in starting_coords])

    return results

sys.setrecursionlimit(1000)
if __name__ == '__main__':
    data = split_strings(read_file('input.txt'))
    max_path = main(data)
    print(max([len(path) for path in max_path]))
