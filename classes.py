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
        self.bridges: list[Bridge] = []
        for i in range(number_of_paths-1):
            if line[i*3+1] == line[i*3+2] == '-':
                self.bridges.append(Bridge(i, i+1))

    def has_bridge_for_path(self, path_name: str) -> bool:
        for bridge in self.bridges:
            if bridge.left == path_name or bridge.right == path_name:
                return True
        return False

    def get_next_path(self, path_name: str) -> int:
        for bridge in self.bridges:
            if bridge.left == path_name:
                return bridge.right
            elif bridge.right == path_name:
                return bridge.left
