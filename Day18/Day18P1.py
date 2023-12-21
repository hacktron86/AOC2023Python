def read_file(file_name):
    data = open(file_name).read().strip()
    return [line.split() for line in data.split('\n')]


def get_path(visited, d, n):
    direction = {
            'U': (-1, 0),
            'R': (0, 1),
            'D': (1, 0),
            'L': (0, -1)
            }
    last_step = visited[-1]
    for _ in range(int(n)):
        next_step = (last_step[0] + direction[d][0],
                     last_step[1] + direction[d][1])
        visited.append(next_step)
        last_step = next_step
    return 


def translate_path(path):
    min_x = min(path, key=lambda point: point[1])[1]
    min_y = min(path, key=lambda point: point[0])[0]

    path = [(y - min_y, x - min_x) for y, x in path]

    return path


def get_bounds(path):
    min_x = min(path, key=lambda x: x[1])[1]
    min_y = min(path, key=lambda x: x[0])[0]
    max_x = max(path, key=lambda x: x[1])[1]
    max_y = max(path, key=lambda x: x[0])[0]

    return [(min_y, min_x), (max_y, max_x)]


def flood_fill(grid, y, x, target, replacement):
    if grid[y][x] != target:
        return

    max_y, max_x = len(grid), len(grid[0])
    stack = [(y, x)]

    while stack:
        current_y, current_x = stack.pop()
        if current_y < 0 or current_y >= max_y or current_x < 0 or current_x >= max_x:
            continue
        if grid[current_y][current_x] != target:
            continue

        grid[current_y][current_x] = replacement

        stack.append((current_y + 1, current_x))
        stack.append((current_y - 1, current_x))
        stack.append((current_y, current_x + 1))
        stack.append((current_y, current_x - 1))


def build_grid(path, height, width):
    grid = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for y, x in path:
        grid[y][x] = 1

    return grid


def find_inside(grid):
    y, x = 0, 0
    max_y = len(grid)
    max_x = len(grid[0])

    while y + 1 < max_y and x + 1 < max_x:
        if grid[y][x] == 1 and grid[y + 1][x + 1] == 0:
            return (y + 1, x + 1)
        y += 1
        x += 1

    raise ValueError("Index outside of the grid size")


def main(data):
    visited = []
    visited.append((0, 0))
    for line in data:
        d, n, _ = line
        get_path(visited, d, n)
    visited = translate_path(list(set(visited)))
    _, max_xy = get_bounds(visited)
    grid = build_grid(visited, *max_xy)
    starting_point = find_inside(grid)
    flood_fill(grid, *starting_point, 0, 1)
    return sum([item for sublist in grid for item in sublist])

total = main(read_file('input.txt'))
print(total)
