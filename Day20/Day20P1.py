from dataclasses import dataclass
from typing import Optional

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

for line in data:
    if line[0][0] == 'broadcaster' or line[0][0] == '%':
        continue
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

for line, value in module_dict.items():
    print(line, value)


def send_pulse(modules, cur_module_name, prev_module_name, pulse, pulse_counts):

    print(prev_module_name, ' -', pulse, '> ', cur_module_name)

    if pulse == 1:
        pulse_counts[0] += 1
    else:
        pulse_counts[1] += 1

    if cur_module_name == 'rx' or cur_module_name == 'output':
        return

    if pulse_counts[0] > 100:
        return

    cur_module = modules[cur_module_name]

    if cur_module.name == 'broadcaster':
        for o in cur_module.outputs:
            send_pulse(modules, o, cur_module.name, 0, pulse_counts)

    if cur_module.ver == '%':
        if pulse == 1:
            return
        else:
            if cur_module.state:
                cur_module.state = 0
                for o in cur_module.outputs:
                    send_pulse(modules, o, cur_module.name, 0, pulse_counts)
            else:
                cur_module.state = 1
                for o in cur_module.outputs:
                    send_pulse(modules, o, cur_module.name, 1, pulse_counts)

    if cur_module.ver == '&':
        cur_module.inputs[prev_module_name] = pulse
        if all(value == 1 for value in cur_module.inputs.values()):
            for o in cur_module.outputs:
                send_pulse(modules, o, cur_module.name, 0, pulse_counts)
        else:
            for o in cur_module.outputs:
                send_pulse(modules, o, cur_module.name, 1, pulse_counts)

    return


high = 0
low = 0
for _ in range(4):
    pulse_counts = [0, 0]
    send_pulse(module_dict, 'broadcaster', 'broadcaster', 0, pulse_counts)
    high += pulse_counts[0]
    low += pulse_counts[1]

print(high * low)

