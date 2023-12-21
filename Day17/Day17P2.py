from heapq import heappush, heappop

def read_file():
    return [list(map(int, line.strip())) for line in open('input.txt')]

data = read_file()

print(data)

visited = set()
prioq = []
prioq.append((0, 0, 0, 0, 0, 0))

while prioq:
    hl, y, x, dy, dx, n = heappop(prioq)

    if y == len(data) -1 and x == len(data[0]) - 1 and n >= 4:
        print(hl)
        break

    if (y, x, dy, dx, n) in visited:
        continue

    visited.add((y, x, dy, dx, n))

    if n < 10 and (dy, dx) != (0, 0):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < len(data) and 0 <= nx < len(data[0]):
            heappush(prioq, (hl + data[ny][nx], ny, nx, dy, dx, n + 1))

    if n >= 4 or (dy, dx) == (0, 0):
        for ndy, ndx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndy, ndx) != (dy, dx) and (ndy, ndx) != (-dy, -dx):
                ny = y + ndy
                nx = x + ndx
                if 0 <= ny < len(data) and 0 <= nx < len(data[0]):
                    heappush(prioq, (hl + data[ny][nx], ny, nx, ndy, ndx, 1))
