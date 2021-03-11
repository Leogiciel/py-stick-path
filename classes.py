class Path:
    def __init__(self, start, end):
        self.start_name = start
        self.end_name = end


class Bridge:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Step:
    def __init__(self, line, number_of_paths):
        self.bridges = []
        for i in range(number_of_paths-1):
            if line[i*3+1] == line[i*3+2] == '-':
                self.bridges.append(Bridge(i, i+1))

    def has_bridge_for_path(self, path):
        for bridge in self.bridges:
            if bridge.left == path or bridge.right == path:
                return True
        return False

    def get_next_path(self, path):
        for bridge in self.bridges:
            if bridge.left == path:
                return bridge.right
            elif bridge.right == path:
                return bridge.left
