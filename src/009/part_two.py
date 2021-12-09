import common


def get_basin(smoke_map, x, y):
    point = int(smoke_map[y][x])


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
                print("Basin size at", x, y, "is", len(basin))
                basins.append(basin)

        print(basins)
        break
