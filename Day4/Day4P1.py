from functools import reduce

with open("input.txt", 'r') as f:
    data = [[[[number
               for number in parts.strip().split(" ")]
              for parts in side.split("|")]
             for side in line.strip().split(":")]
            for line in f if line.strip()]

sum = 0
for line in data:
    for side in line[1:]:
        intersection = reduce(lambda acc, x: acc + [x]
                              if x in side[0] and x not in acc
                              else acc, side[1], [])
        filtered_intersection = [item for item in intersection if item]
        points = 0
        print(filtered_intersection)
        if len(filtered_intersection) > 0:
            points = reduce(lambda acc, _:
                            acc * 2, filtered_intersection[1:], 1)
        sum += points
        print(points)

print(sum)
