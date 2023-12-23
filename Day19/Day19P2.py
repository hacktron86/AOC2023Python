import math
import operator
from dataclasses import dataclass


@dataclass
class Workflow():
    name: str 
    rules: list[tuple[str, str]] 
    
    ops = {
        ">": operator.gt,
        "<": operator.lt,
    }

    @staticmethod
    def parse_condition(condition):
        op = next(op for op in Workflow.ops if op in condition)
        left_operand, right_operand = condition.split(op)
        return left_operand, op, int(right_operand)
    
    def execute(self, part: dict):
        for condition, next_flow in self.rules:
            if condition[0] in "xmas":
                left, op, right = self.parse_condition(condition)
                part_val = part[left]
                res = Workflow.ops[op](part_val, right)
            else:
                res = True
            
            if res:
                return next_flow
        
        assert False


def parse_input(data: str) -> dict[str,Workflow]:
    flow_lines, _ = [block.splitlines() for block in data.split("\n\n")]
    
    workflows = {}
    for flow_line in flow_lines:
        flow_name, flow_rules = flow_line.split("{")
        flow_rules = flow_rules.strip("}")
        flow_rules = [flow_rule for flow_rule in flow_rules.split(",")]
        
        new_rules = []
        for rule in flow_rules:
            if ":" in rule:
                new_rules.append(tuple(rule.split(":")))
            else:
                new_rules.append(("True", rule))
                
        workflows[flow_name] = Workflow(flow_name, new_rules)
    
    return workflows


def count_ranges(ranges, wf_name, wfs):
    if wf_name in ["R", "A"]:
        return 0 if wf_name == "R" else math.prod(h-l+1 for l, h in ranges.values())
    
    total = 0
    for cond, nxt in wfs[wf_name].rules:
        if cond[0] in "xmas":
            cat, op, rv = Workflow.parse_condition(cond)
            l, h = ranges[cat]
            t_cond = (l, rv-1) if op == "<" else (rv+1, h)
            f_cond = (rv, h) if op == "<" else (l, rv)
            if t_cond[0] <= t_cond[1]: 
                rc = dict(ranges); rc[cat] = t_cond
                total += count_ranges(rc, nxt, wfs) 
            ranges = {**ranges, cat: f_cond} if f_cond[0] <= f_cond[1] else ranges
        else:
            assert cond == "True", "Final condition check."
            total += count_ranges(ranges, nxt, wfs)
    return total


def part2(data):
    workflows = parse_input(data)
    
    ranges = { cat: (1, 4000) for cat in "xmas" }
    workflow_name = "in"
    accepted = count_ranges(ranges, workflow_name, workflows)
    
    return accepted


res = part2(open(0).read())
print(res)
