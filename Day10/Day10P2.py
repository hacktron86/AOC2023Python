import numpy as np
from collections import deque

lines = open("input.txt").readlines()
data = np.pad(
        np.array([[char for char in line.strip()]
                  for line in [x.strip() for x in lines]]),
        1,
        constant_values=".",
        )
connections = {
        "-": [(0, -1), (0, 1)],
        "|": [(-1, 0), (1, 0)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [],
        }
delta_s = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
point = np.array(next(zip(*np.where(data == "S"))))
(lx, lv), (rx, rv) = [
        (point + delta, delta)
        for delta in delta_s if tuple(-delta) in
        connections[data[tuple(point + delta)]]
        ]


def update(point, direction):
    options = connections[data[tuple(point)]]
    new_direction = np.array(
            options[1] if tuple(-direction) == options[0] else options[0]
            )
    return point + new_direction, new_direction


i = 1
left_path = [point, lx]
right_path = [rx]
while not np.allclose(lx, rx):
    lx, lv = update(lx, lv)
    left_path.append(lx)
    rx, rv = update(rx, rv)
    right_path.append(rx)
    i += 1
i

ys, xs = zip(*(left_path + right_path[:-1][::-1]))
dy, dx = np.diff([ys + (ys[0],), xs + (xs[0],)], axis=1)
board = np.ones((data.shape[0] * 2, data.shape[1] * 2))
ys, xs = map(np.array, [ys, xs])
board[2 * ys, 2 * xs] = 0

board[2 * ys + dy, 2 * xs + dx] = 0
board = np.pad(board[1:-1, 1:-1], 1, constant_values=0)
points = deque([(1, 1)])
while points:
    point = points.popleft()
    if board[point] == 0:
        continue
    board[point] = 0
    for delta in delta_s:
        nb = tuple(delta + point)
        if board[nb]:
            points.append(nb)
print(int(board[::2, ::2].sum()))
