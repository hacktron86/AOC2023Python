import matplotlib.pyplot as plt
import matplotlib.cm as cm
bricks =  [[[int(x) for x in y.split(',')] 
            for y in line.split('~')]
                for line in open(0).read().split()]


def get_bounds(bricks):

    maxx, maxy, maxz = 0, 0, 0

    for brick in bricks:
        maxx = max(maxx, brick[0][0] + brick[1][0] - brick[0][0])
        maxy = max(maxy, brick[0][1] + brick[1][1] - brick[0][1])
        maxz = max(maxz, brick[0][2] + brick[1][2] - brick[0][2])

    print(maxx, maxy, maxz)


    return [maxx, maxy, maxz]


def build_cube(bricks):

    maxx, maxy, maxz = get_bounds(bricks)

    cube =  [
                [
                    [
                        0 for _ in range(maxx + 1)
                    ]
                    for _ in range(maxy + 1)
                ]
                for _ in range(maxz + 1)
            ]

    brickCount = 0
    for brick in bricks:
        brickCount += 1
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for z in range(brick[0][2], brick[1][2] + 1):
                    cube[z][y][x] = brickCount

    return cube, [maxx, maxy, maxz]


tower, bounds = build_cube(bricks)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colormap = plt.get_cmap('viridis')

for z, layer in enumerate(tower):
    for y, row in enumerate(layer):
        for x, brick in enumerate(row):
            if brick != 0:
                ax.scatter(x, y, z, color=colormap(brick / len(bricks)), marker='s')

ax.set_xticks([x for x in range(bounds[0])])
ax.set_yticks([y for y in range(bounds[1])])
ax.set_zticks([z for z in range(bounds[2])])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

plt.show()
