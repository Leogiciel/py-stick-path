from classes import Path
from classes import Step
import unittest


def get_steps(height, lines, number_of_paths):
    steps = []
    for i in range(2, height):
        steps.append(Step(lines[i], number_of_paths))
    return steps


def get_dimensions(line):
    parsed_line = line.split(' ')
    width = int(parsed_line[0])
    height = int(parsed_line[1])
    return height, width


def get_paths(height, lines, width):
    paths = []
    number_of_paths = int(1 + (width - 1) / 3)
    start_name_line = lines[1].replace(' ', '')
    end_name_line = lines[height].replace(' ', '')
    for i in range(number_of_paths):
        paths.append(Path(start_name_line[i], end_name_line[i]))
    return paths
