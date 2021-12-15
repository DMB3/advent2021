import common


class Graph:
    def __init__(self):
        self.connections = {}
        self.cost_to_enter = {}

        self.width = -1
        self.height = -1

    def add(self, start, end):
        self.width = max(self.width, start[0] + 1, end[0] + 1)
        self.height = max(self.height, start[1] + 1, end[1] + 1)

        if start not in self.connections:
            self.connections[start] = set()
        self.connections[start].add(end)

        if end not in self.connections:
            self.connections[end] = set()
        self.connections[end].add(start)

    def dijkstra(self, start, end):
        shortest = {start: (None, 0)}
        current = start
        visited = set()

        while current != end:
            visited.add(current)
            destinations = self.connections.get(current, [])
            cost = shortest[current][1]

            for following in destinations:
                following_cost = self.cost_to_enter[following] + cost
                if following not in shortest:
                    shortest[following] = (current, following_cost)
                else:
                    current_cost = shortest[following][1]
                    if current_cost > following_cost:
                        shortest[following] = (current, following_cost)

            next_destinations = {node: shortest[node] for node in shortest if node not in visited}
            if not next_destinations:
                # path is not doable
                return None

            current = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        current_cost = None
        while current is not None:
            path.append((current, current_cost))
            current, current_cost = shortest[current]

        return path[::-1]


if __name__ == "__main__":
    for input_file in common.inputs:
        lines = []
        for line in common.read_file(input_file):
            lines.append(line)

        graph = Graph()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if x + 1 < len(lines[y]):
                    graph.add((x, y), (x + 1, y))
                if y + 1 < len(lines):
                    graph.add((x, y), (x, y + 1))
                if x - 1 >= 0:
                    graph.add((x - 1, y), (x, y))
                if y - 1 >= 0:
                    graph.add((x, y - 1), (x, y))

                graph.cost_to_enter[(x, y)] = int(lines[y][x])

        path = graph.dijkstra((0, 0), (graph.width - 1, graph.height - 1))
        cost = path[-2][1]

        print(f"Cost for {input_file} is {cost}")
