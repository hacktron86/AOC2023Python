from collections import deque

grid = open(0).read().splitlines()

sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

steps = 26501365
size = len(grid)
original = steps % (2 * size)

def take_steps(x):
    ans = set()
    seen = {(sr, sc)}
    q = deque([(sr, sc, original + 2 * size * x)])

    while q:
        r, c, s = q.popleft()

        if s % 2 == 0:
            ans.add((r, c))
        if s == 0:
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if grid[nr % size][nc % size] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr, nc))
            q.append((nr, nc, s - 1))

    return len(ans)



values = []
x = 0

while True:
    values.append(take_steps(x))
    x += 1

    if len(values) >= 4:
        fd = [values[1] - values[0], values[2] - values[1], values[3] - values[2]]
        sd = [fd[1] - fd[0], fd[2] - fd[1]]
        if sd[0] == sd[1]:
            break
        else:
            values.pop(0)


offset = x - 4

alpha, beta, gamma, _ = values

c = alpha
a = (gamma - 2 * beta + c) / 2
b = beta - c - a 

def f(x):
    return a * x ** 2 + b * x + c

print(f(steps // (2 * size) - offset))
