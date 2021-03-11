import paths_parser


def compute_paths(args):
    lines = args.splitlines()
    height, width = paths_parser.get_dimensions(lines[0])
    paths = paths_parser.get_paths(height, lines, width)
    steps = paths_parser.get_steps(height, lines, len(paths))
    result = ""
    for i in range(len(paths)):
        result += compute_path(paths, steps, i)
    return result


def compute_path(paths, steps, i):
    result = [paths[i].start_name, paths[i].end_name]
    actual_path = i
    actual_end_path = i
    for j in range(len(steps)):
        step = steps[j]
        if step.has_bridge_for_path(actual_path):
            actual_path = actual_end_path = step.get_next_path(actual_path)
    result[1] = paths[actual_end_path].end_name
    return f'{result[0]}{result[1]}\n'

