from dataclasses import dataclass
from typing import Optional
from collections import deque

def read_file():
    data = open(0).read().strip().replace(' -> ', ';')
    return  [
                [
                    [a[0], a[1:].strip()] if a[0] == '&' else
                    [a[0], a[1:].strip(), 0] if a[0] == '%' else
                    ['broadcaster', a.strip()] if a == 'broadcaster' else 
                    [i.strip() for i in a.split(',')]
                    for a in line.split(';')
                ]
                for line in data.split('\n')
            ]

@dataclass
class Module:
    name: str
    ver: str
    state: Optional[bool] = None
    inputs: Optional[dict[str, int]] = None
    outputs: Optional[list[str]] = None

    def __post_init__(self):
        if self.inputs is None:
            self.inputs = {}
        if self.outputs is None:
            self.outputs = []
    

data = read_file()

input_dict = {}

#print(data)

for line in data:
    if line[0][0] == 'broadcaster':
        continue
    #print(line[1])
    for output in line[1]:
        if output not in input_dict:
            input_dict[output] = []
        input_dict[output].append(line[0][1])


module_dict = {
        module[1]: Module(
            name = module[1],
            ver = module[0],
            state = bool(module[2]) if len(module) > 2 else False,
            outputs = outputs
            )
        for module, outputs in data
        }

for key in module_dict:
    if key in input_dict:
        module_dict[key].inputs = {a: 0 for a in input_dict[key]}

#for line, value in input_dict.items():
#    print(line, value)
#
#for line, value in module_dict.items():
#    print(line, value)


def hit_button(modules, pulse_counts):

    queue = deque()
    queue.append(['broadcaster', 'button', 0])

    while queue:

        cur, prev, pulse = queue.popleft()

        #print(prev, ' -', ('high' if pulse else 'low'), '> ', cur)

        if pulse == 1:
            pulse_counts[0] += 1
        else:
            pulse_counts[1] += 1

        if cur == 'rx' or cur == 'output':
            continue

        module = modules[cur]
        
        #print(module)

        if module.name == 'broadcaster':
            for output in module.outputs:
                queue.append([output, cur, 0])

        if module.ver == '%':
            if pulse == 1:
                continue
            else:
                if module.state:
                    module.state = 0
                    for output in module.outputs:
                        queue.append([output, cur, 0])
                else:
                    module.state = 1
                    for output in module.outputs:
                        queue.append([output, cur, 1])

        if module.ver == '&':
            module.inputs[prev] = pulse
            if all(value == 1 for value in module.inputs.values()):
                for output in module.outputs:
                    queue.append([output, cur, 0])
            else:
                for output in module.outputs:
                    queue.append([output, cur, 1])


high = 0
low = 0
for _ in range(1000):
    pulse_counts = [0, 0]
    #print()
    hit_button(module_dict, pulse_counts)
    high += pulse_counts[0]
    low += pulse_counts[1]

print(high * low)

