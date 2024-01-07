import matplotlib.pyplot as plt


def get_bricks():
    return [[[int(x) for x in y.split(',')] 
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



def build_cube(bricks, bounds):

    cube = build_empty_cube(*bounds)

    brickCount = 0
    for brick in bricks:
        brickCount += 1
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for z in range(brick[0][2], brick[1][2] + 1):
                    cube[z][y][x] = brickCount

    return cube


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

def get_brick_coords(tower, brick):

    brick_coords = []
    for z, layer in enumerate(tower):
        for y, col in enumerate(layer):
            for x, row in enumerate(col):
                if row == brick:
                    brick_coords.append([z, x, y])

    return brick_coords


def test_drop(player, bcoords):

    for x, y in bcoords:
        if player[y][x] != 0:
            return False

    return True


def drop_brick(layer, prevlayer, brick_coords, brick):

    for x, y in brick_coords:
        prevlayer[y][x] = brick
        layer[y][x] = 0


def check_layer(tower, layer, prevlayer):

    for row in layer:
        prevbrick = 0
        for brick in row:
            if brick == 0:
                continue
            if brick == prevbrick:
                continue
            print(tower, brick)
            brick_coords = get_brick_coords(tower, brick)
            print(brick_coords)
            min_z = min(c[0] for c in brick_coords)
            brick_coords = [c for c in brick_coords if c[0] == min_z]
            can_drop = test_drop(prevlayer, brick_coords)
            if can_drop:
                drop_brick(layer, prevlayer, brick_coords, brick)
            prevbrick = brick


def drop_tower(tower):

    prevlayer = []
    first_found = False
    newtower = []
    while tower:
        layer = tower.pop(0)
        if all(el == 0 for row in layer for el in row):
            continue
        if not first_found:
            first_found = True
            newtower.append(layer)
            prevlayer = layer
            continue
        check_layer(tower, layer, prevlayer)
        if not all(el == 0 for row in layer for el in row):
            newtower.append(layer)
            prevlayer = layer

    return newtower


def test_supports(layer, brick_coords):

    bricks = []
    for x, y in brick_coords:
        brick = layer[y][x]
        if brick != 0:
            if brick not in bricks:
                bricks.append(brick)

    if len(bricks) > 1:
        return True

    return False


def can_disintegrate(prevlayer, layer, brick_coords):

    print(f"player {prevlayer}")
    print(f"layer {layer}")

    bricks = []
    for x, y in brick_coords:
        brick = layer[y][x]
        if brick != 0:
            if brick not in bricks:
                bricks.append(brick)
    print(bricks)
    for brick in bricks:
        if not test_supports(prevlayer, get_brick(layer, brick)):
            return False

    return True


def safe_bricks(tower):

    safe = 0
    prevlayer = []
    bricks = []
    for z, layer in enumerate(tower):
        print(z)
        if not prevlayer:
            prevlayer = layer
            continue
        for row in layer:
            for brick in row:
                if brick == 0:
                    continue
                if brick in bricks:
                    continue
                print(f"Brick {brick} found")
                brick_coords = get_brick(layer, brick)
                print(f"Length of tower {len(tower)} z {z}")
                if can_disintegrate(layer, tower[z+1], brick_coords):
                    print(f"Brick {brick} safe")
                    safe += 1
                bricks.append(brick)
        prevlayer = layer
    return safe


bricks = get_bricks()
bounds = get_bounds(bricks)
tower = build_cube(bricks, bounds)
#show_plot(tower, bricks, bounds)
dtower = drop_tower(tower)
#print(tower)
for layer in reversed(dtower):
    print(layer)
#show_plot(dtower, bricks, bounds)
res = safe_bricks(dtower)
print(res)
