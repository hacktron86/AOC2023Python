from os import WSTOPSIG
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

    return [maxx, maxy, maxz]


def build_empty_cube(x, y, z):
    cube =  [
                [
                    [
                        0 for _ in range(x + 1)
                    ]
                    for _ in range(y + 1)
                ]
                for _ in range(z + 1)
            ]

    return cube



def build_cube(bricks):

    maxx, maxy, maxz = get_bounds(bricks)

    cube = build_empty_cube(maxx, maxy, maxz)

    brickCount = 0
    for brick in bricks:
        brickCount += 1
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for z in range(brick[0][2], brick[1][2] + 1):
                    cube[z][y][x] = brickCount

    return cube, [maxx, maxy, maxz]


def show_plot(tower, bricks, bounds):
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
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')

    plt.show()


def get_brick(layer, brick):

    bcoords = []
    for y, col in enumerate(layer):
        for x, row in enumerate(col):
            if row == brick:
                bcoords.append([x, y])

    return bcoords


def test_drop(player, bcoords):

    for x, y in bcoords:
        if player[y][x] != 0:
            return False

    return True


def drop_tower(tower, bounds):

    prevlayer = []
    mx, my, mz = bounds
    newtower = build_empty_cube(mx, my, mz)
    for z, layer in enumerate(tower):

        if all(el == 0 for row in layer for el in row):
            continue
        if not prevlayer:
            newtower[z] = layer
            prevlayer = layer
            continue
        for y, row in enumerate(layer):
            prevbrick = 0
            for x, brick in enumerate(row):
                if brick == 0:
                    continue
                if brick == prevbrick:
                    continue
                brick_coords = get_brick(layer, brick)
                can_drop = test_drop(tower[z-1], brick_coords)
                if can_drop:
                    print("Drop")
                    print(z, layer, brick)
                else:
                    print("Stay")
                    print(z, layer, brick)
                prevbrick = brick
        prevlayer = layer

    return newtower


tower, bounds = build_cube(bricks)
#show_plot(tower, bricks, bounds)
dtower = drop_tower(tower, bounds)
print(tower)
print(dtower)
