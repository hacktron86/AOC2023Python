with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n\n')

inputs = [int(x) for x in data[0].replace("seeds: ", "").split(" ")]

seeds = [(inputs[i], inputs[i] + inputs[i + 1])
         for i in range(0, len(inputs), 2)]

maps = [[[int(y)
          for y in x.split(" ")]
         for x in data[i].splitlines()[1:]]
        for i in range(1, 8)
        ]


def remap(start, end, new_seeds, m) -> int:
    for dst, strt, rnge in m:
        overlap_s = max(start, strt)
        overlap_e = min(end, strt + rnge)

        if overlap_s < overlap_e:
            new_seeds.append(
                    (
                        dst + overlap_s - strt,
                        dst + overlap_e - strt
                    )
                    )

            if start < overlap_s:
                seeds.append((start, overlap_s))

            if overlap_e < end:
                seeds.append((overlap_e, end))

            break
    else:
        new_seeds.append((start, end))


for m in maps:
    new_seeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        remap(start, end, new_seeds, m)

    seeds = new_seeds

print(min(seeds)[0])
