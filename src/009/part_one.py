import common


def is_low_point(smoke_map, x, y):
    point = int(smoke_map[y][x])

    if x - 1 >= 0:
        if int(smoke_map[y][x - 1]) <= point:
            return False, point
    if y - 1 >= 0:
        if int(smoke_map[y - 1][x]) <= point:
            return False, point
    if x + 1 < len(smoke_map[0]):
        if int(smoke_map[y][x + 1]) <= point:
            return False, point
    if y + 1 < len(smoke_map):
        if int(smoke_map[y + 1][x]) <= point:
            return False, point

    return True, point


if __name__ == "__main__":
    for input_file in common.inputs:
        smoke_map = []
        risk_sum = 0

        for line in common.read_file(input_file):
            smoke_map.append(line)

        for y in range(len(smoke_map)):
            for x in range(len(smoke_map[y])):
                low, point = is_low_point(smoke_map, x, y)
                if low:
                    risk_sum += (point + 1)

        print(f"The sum of risk levels for low points in {input_file} is {risk_sum}")
