from classes import Path
from classes import Step
from typing import Tuple


def get_steps(height: int, lines: [str], number_of_paths: int) -> [Step]:
    steps = []
    for i in range(2, height):
        steps.append(Step(lines[i], number_of_paths))
    return steps


def get_dimensions(line: str) -> Tuple[int, int]:
    parsed_line = line.strip().split(' ')
    if len(parsed_line) != 2:
        raise ValueError(f'Dimensions line must contain 2 elements, '
                         f'dimension line received : [{line}] returned [{len(parsed_line)}] elements')
    try:
        width = int(parsed_line[0])
        height = int(parsed_line[1])
    except ValueError as ve:
        raise ValueError(f'A dimension is not valid : {ve}')
    if width < 4:
        raise ValueError(f'Invalid value received for width : received [{width}], must be over 3')
    if height < 1 or height > 100:
        raise ValueError(f'Invalid value received for height : received [{height}], must be between 1 and 100')
    return height, width


def check_line(line: str, length: int) -> None:
    if len(line) != length:
        raise ValueError(f'Line [{line}] does not have required values length [{length}]')


def get_paths(height: int, lines: [str], width: int) -> [Path]:
    paths = []
    # standard format implies width % 3 == 1
    number_of_paths = int(1 + (width - 1) / 3)
    # removing spaces to work on values ranks
    top_values_line = lines[1].replace(' ', '')
    bottom_values_line = lines[height].replace(' ', '')
    check_line(top_values_line, number_of_paths)
    check_line(bottom_values_line, number_of_paths)
    for i in range(number_of_paths):
        paths.append(Path(top_values_line[i], bottom_values_line[i]))
    return paths
