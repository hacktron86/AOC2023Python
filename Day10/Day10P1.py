with open("input.txt") as f:
    data = [list(char) for char in f.read().splitlines()]

pipe_dict = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
    ".": [],
    "S": ["N", "S", "E", "W"],
}

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = [i, j]
            break


def check_paths(pos):
    x, y = pos
    cur_pipe = data[x][y]
    print("Coords: ", pos)
    print("Current Pipe: ", cur_pipe)
    # check up
    if pos[0] > 0:
        print("Up Pipe: ", data[x-1][y])
        pipe = data[x-1][y]
        if ("S" in pipe_dict[pipe] and
            "N" in pipe_dict[cur_pipe] and
                "S" != prev):
            return "N"
    # check left
    if pos[1] > 0:
        print("Left Pipe: ", data[x][y-1])
        pipe = data[x][y-1]
        if ("E" in pipe_dict[pipe] and
            "W" in pipe_dict[cur_pipe] and
                "E" != prev):
            return "W"
    # check right
    if pos[1] < len(data[0])-1:
        print("Right Pipe: ", data[x][y+1])
        pipe = data[x][y+1]
        if ("W" in pipe_dict[pipe] and
            "E" in pipe_dict[cur_pipe] and
                "W" != prev):
            return "E"
    # check down
    if pos[0] < len(data)-1:
        print("Down Pipe: ", data[x+1][y])
        pipe = data[x+1][y]
        if ("N" in pipe_dict[pipe] and
            "S" in pipe_dict[cur_pipe] and
                "N" != prev):
            return "S"
    # throw error no path exists
    raise ValueError("No path exists")


def move_direction(direction):
    if direction == "N":
        pos[0] -= 1
        return
    if direction == "W":
        pos[1] -= 1
        return
    if direction == "E":
        pos[1] += 1
        return
    if direction == "S":
        pos[0] += 1
        return
    raise ValueError("Invalid direction")


end = ""
pos = start
count = 0
direction = ""
while end != "S":
    print(data[pos[0]][pos[1]])
    prev = direction
    direction = check_paths(pos)
    print("Direction: " + direction)
    print("Current Pipe: ", data[pos[0]][pos[1]], "\n", "Coord: ", pos)
    move_direction(direction)
    print("Next Pipe: ", data[pos[0]][pos[1]], "\n", "Coord: ", pos)
    end = data[pos[0]][pos[1]]
    count += 1


print(count/2)
