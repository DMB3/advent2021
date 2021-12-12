import common


class Graph:
    def __init__(self):
        self.nodes = set()
        self.connections = {}

    def __repr__(self):
        return f"Nodes({self.nodes}), Connections({self.connections})"

    def add_connection(self, source, target):
        if source not in self.nodes:
            self.nodes.add(source)
            self.connections[source] = []

        if target not in self.nodes:
            self.nodes.add(target)
            self.connections[target] = []

        self.connections[source].append(target)
        self.connections[target].append(source)

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.connections:
            return []

        paths = []
        for node in self.connections[start]:
            if (node not in path) or (node in path and node.isupper()):
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths


if __name__ == "__main__":
    for input_file in common.inputs:
        graph = Graph()

        for line in common.read_file(input_file):
            start, end = line.split("-")
            graph.add_connection(start, end)

        paths = graph.find_all_paths("start", "end")
        print(f"There are {len(paths)} paths between start and end in {input_file}")
