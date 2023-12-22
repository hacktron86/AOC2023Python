def read_file(file_name):
    with open(file_name) as f:
        sections = f.read().strip().split('\n\n')
    return [line.split('\n') for line in sections]


def parse_workflows(workflows_raw):
    workflows = {}
    for workflow in workflows_raw:
        name, steps = list(workflow.replace('}', '').split('{'))
        steps_list = steps.split(',')
        parsed_steps = []
        parsed_steps.append(steps_list[-1])
        for step in steps_list[:-1]:  # Process all but the last sublist
            if ':' in step:
                sub_steps = step.split(':')
                # Splitting the first item of the sublist as required
                first_part = sub_steps[0]
                if '<' in first_part:
                    split_first_part = first_part.split('<')
                    sub_steps[0] = [split_first_part[0], '<', split_first_part[1]]
                elif '>' in first_part:
                    split_first_part = first_part.split('>')
                    sub_steps[0] = [split_first_part[0], '>', split_first_part[1]]
                parsed_steps.append(sub_steps)
            else:
                parsed_steps.append(step)
        workflows[name] = parsed_steps
    return workflows


def parse_parts(parts_raw):
    parts = []
    for part in parts_raw:
        properties = part[1:-1].split(',')
        props = {}
        for property in properties:
            key, value = property.split('=')
            props[key] = int(value)
        parts.append(props)

    return parts


def main():
    workflows_raw, parts_raw = read_file(0)
    workflows = parse_workflows(workflows_raw)
    parts = parse_parts(parts_raw)

    accepted_parts = []
    for part in parts:
        default = 'in'
        next_wf = default

        while True:
            if next_wf == 'A' or next_wf == 'R':
                break
            fallback, *wfs = workflows[next_wf]
            for wf in wfs:
                condition, result = wf
                prop, opr, n = condition
                if opr == '>':
                    if part[prop] > int(n):
                        next_wf = result
                        break
                else:
                    if part[prop] < int(n):
                        next_wf = result
                        break
                next_wf = fallback

        if next_wf == 'A':
            accepted_parts.append(part)

    total_sum = sum(sum(d.values()) for d in accepted_parts)
    print(total_sum)


main()
