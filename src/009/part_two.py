import common


def get_basin(smoke_map, x, y, visited=[]):
    point = int(smoke_map[y][x])
    visited.append((x, y))

    if point == 9:
        return []

    result = [(x, y)]
    if x - 1 >= 0 and (x - 1, y) not in visited:
        result += get_basin(smoke_map, x - 1, y, visited=visited)
    if x + 1 < len(smoke_map[0]) and (x + 1, y) not in visited:
        result += get_basin(smoke_map, x + 1, y, visited=visited)
    if y - 1 >= 0 and (x, y - 1) not in visited:
        result += get_basin(smoke_map, x, y - 1, visited=visited)
    if y + 1 < len(smoke_map) and (x, y + 1) not in visited:
        result += get_basin(smoke_map, x, y + 1, visited=visited)

    return result


if __name__ == "__main__":
    for input_file in common.inputs:
        smoke_map = []
        basins = []

        for line in common.read_file(input_file):
            smoke_map.append(line)

        for y in range(len(smoke_map)):
            for x in range(len(smoke_map[y])):
                point = int(smoke_map[y][x])

                if point == 9:
                    continue

                basin = get_basin(smoke_map, x, y)
                basins.append((len(basin), basin))

                for bx, by in basin:
                    smoke_map[by] = smoke_map[by][:bx] + "9" + smoke_map[by][bx + 1:]

        basins = sorted(basins)[::-1]
        one, two, three = basins[0][0], basins[1][0], basins[2][0]
        result = one * two * three

        print(f"For {input_file} largest basins are {one}, {two} and {three} and result is {result}")
