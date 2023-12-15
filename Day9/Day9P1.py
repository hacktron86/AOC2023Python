import numpy as np

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

lines = np.array([[int(item.strip()) for item in line.split()]
                  for line in lines], dtype=int)

newlines = np.array(0)

sum = 0
for line in lines:
    found = False
    newline = np.empty(0, dtype=int)
    cur = line
    print(line)
    toadd = np.empty(0, dtype=int)
    while not found:
        toadd = np.append(toadd, cur[-1])
        diff = np.diff(cur)
        print(diff)
        if np.sum(diff) == 0:
            found = True
        cur = diff

    print(toadd)
    final = np.sum(toadd)
    print(final)
    sum += final
    print(sum)


print(sum)
