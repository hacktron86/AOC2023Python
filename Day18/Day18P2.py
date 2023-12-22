def read_file(file_name):
    data = open(file_name)
    return [line.split() for line in data]


def get_path(path, d, n):
    direction = {
            3: (-1, 0),   # U
            0: (0, 1),    # R
            1: (1, 0),    # D
            2: (0, -1)    # L
            }
    prev = path[-1]
    path.append((prev[0] + (direction[d][0] * n),
                 prev[1] + (direction[d][1] * n)))


def main(data):
    path = []
    path.append((0, 0))
    b = 0
    for line in data:
        _, _, h = line
        n, d = int(h[2:7], 16), h[7:-1]
        b += int(n)
        get_path(path, int(d), int(n))
    A = abs(sum(path[i][0] * (path[i - 1][1] - path[(i + 1) % len(path)][1]) 
                for i in range(len(path)))) // 2
    i = A - b // 2 + 1
    return i + b


result = main(read_file('input.txt'))
print(result)
