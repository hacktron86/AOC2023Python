def read_file():
    data = open(0).read().strip()
    data = [list(line) for line in data.split('\n')]
    return data


def check_valid(p, d, g):
    y = p[0] + d[0]
    x = p[1] + d[1]
    if y > len(g) or y < 0:
        return False
    if x > len(g[0]) or x < 0:
        return False
    if g[y][x] == '#':
        return False
    return True


def start_walking(grid, steps):

    start = [
                (i, j) for i, row in enumerate(grid)
                for j, item in enumerate(row) if item == 'S'
            ][0]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    positions = []
    positions.append(start)

    while steps:

        new_p = []

        for p in positions:
            for d in directions:
                if check_valid(p, d, grid):
                    new_p.append((p[0] + d[0], p[1] + d[1]))

        positions = list(set(new_p))

        steps -= 1

    return positions


def main():
    grid = read_file()

    steps = 64
    pos = start_walking(grid, steps)

    print(len(pos))


main()
