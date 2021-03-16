from typing import List

import paths_parser
from classes import Path, Step


def compute_paths(args: str) -> str:
    # check argument type
    if type(args) is not str:
        raise ValueError(f"Argument must be a string, not {type(args)}")
    lines = args.splitlines()
    if len(lines) < 4:
        raise ValueError(
            f"Argument must contains at least 4 lines :"
            f" [{args}] contains only [{len(lines)}] lines"
        )
    # extract array dimensions
    height, width = paths_parser.get_dimensions(lines[0])
    # build paths array (top and bottom values)
    paths = paths_parser.get_paths(height, lines, width)
    # build steps array (steps will contain bridges)
    steps = paths_parser.get_steps(height, lines, len(paths))
    result = "\n".join([compute_path(paths, steps, i) for i in range(len(paths))])
    return result


def compute_path(paths: List[Path], steps: List[Step], i: int) -> str:
    # default path if no bridge
    result = [paths[i].top_value, paths[i].bottom_value]
    actual_path = i
    actual_end_path = i
    # for each step
    for j in range(len(steps)):
        step = steps[j]
        actual_path = actual_end_path = step.get_next_path(actual_path)
    # update final result
    result[1] = paths[actual_end_path].bottom_value
    return f"{result[0]}{result[1]}"
