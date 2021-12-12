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
            is_big = node.isupper()

            if node == "start":
                # we can't get back to the start
                can_visit = False
            elif is_big:
                # we can visit big caves however many times we want
                can_visit = True
            else:
                visit_limit = 2

                # have we visited any other small cave twice?
                any_other_lower = any([piece != "start" and
                                       piece.islower() and
                                       piece != node and
                                       path.count(piece) == 2 for piece in path])
                if any_other_lower:
                    visit_limit = 1

                # how many times have we visited this one before
                this_before = path.count(node)
                can_visit = this_before <= visit_limit - 1

            if can_visit:
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
