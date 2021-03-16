class Path:
    def __init__(self, start: str, end: str):
        self.top_value: str = start
        self.bottom_value: str = end


class Bridge:
    def __init__(self, left: int, right: int):
        self.left: int = left
        self.right: int = right


class Step:
    def __init__(self, line: str, number_of_paths: int):
        self.bridges: list[Bridge] = [
            Bridge(i, i + 1)
            for i in range(number_of_paths - 1)
            if line[i * 3 + 1] == line[i * 3 + 2] == "-"
        ]

    def get_next_path(self, path_rank: int) -> int:
        for bridge in self.bridges:
            if bridge.left == path_rank:
                return bridge.right
            if bridge.right == path_rank:
                return bridge.left
        return path_rank
