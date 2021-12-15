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

    def breadth_first(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        MAX = 2e10

        costs = {start_y: {
            start_x: 0
        }}

        in_queue = [start]
        while len(in_queue) > 0:
            first_element = in_queue.pop(0)
            first_x, first_y = first_element

            for connected in self.connections[first_element]:
                connected_x, connected_y = connected

                connected_cost = costs.get(connected_y, {}).get(connected_x, MAX)
                cost_to_connected = costs.get(first_y, {}).get(first_x, MAX) + self.cost_to_enter[
                    connected]

                if connected_cost > cost_to_connected:
                    if connected_y not in costs:
                        costs[connected_y] = {}

                    costs[connected_y][connected_x] = cost_to_connected
                    in_queue.append(connected)

        return costs[end_y][end_x]


def repeat_line(line):
    result = ""

    for character in line:
        value = int(character) + 1
        if value > 9:
            value = 1
        result = "%s%d" % (result, value)

    return result


if __name__ == "__main__":
    for input_file in common.inputs:
        lines = []

        for line in common.read_file(input_file):
            lines.append(line)

        one_repeat = []
        two_repeat = []
        three_repeat = []
        four_repeat = []
        for line in lines:
            two = repeat_line(line)
            three = repeat_line(two)
            four = repeat_line(three)
            five = repeat_line(four)

            one_repeat.append(two)
            two_repeat.append(three)
            three_repeat.append(four)
            four_repeat.append(five)

        lines += one_repeat
        lines += two_repeat
        lines += three_repeat
        lines += four_repeat

        new_lines = []
        for line in lines:
            two = repeat_line(line)
            three = repeat_line(two)
            four = repeat_line(three)
            five = repeat_line(four)
            new_lines.append(line + two + three + four + five)

        lines = new_lines
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

        cost = graph.breadth_first((0, 0), (graph.width - 1, graph.height - 1))
        print(f"Cost for {input_file} is {cost}")
