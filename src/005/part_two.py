import common


def print_map(vent_map, width, height):
    for y in range(height + 1):
        if y not in vent_map:
            vent_map[y] = {}

        line = ""
        for x in range(width + 1):
            if x not in vent_map[y]:
                vent_map[y][x] = 0

            piece = 0 if x not in vent_map[y] else vent_map[y][x]
            line += "%d" % (piece,)
        print(line)


def add_vent(vent_map, x, y):
    if y not in vent_map:
        vent_map[y] = {}
    if x not in vent_map[y]:
        vent_map[y][x] = 0

    vent_map[y][x] += 1


if __name__ == "__main__":
    for input_file in common.inputs:
        vent_map = {}
        width, height = 0, 0
        count = 0
        already_counted = set()
        for line in common.read_file(input_file):
            one, two = line.strip().split("->")
            (x0, y0), (x1, y1) = one.split(","), two.split(",")
            x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

            width = max(width, x0, x1)
            height = max(height, y0, y1)

            x, y = (x0, y0)
            while True:
                add_vent(vent_map, x, y)

                if vent_map[y][x] >= 2 and (x, y) not in already_counted:
                    count += 1
                    already_counted.add((x, y))

                if (x, y) == (x1, y1):
                    break

                if x > x1:
                    x -= 1
                elif x < x1:
                    x += 1

                if y > y1:
                    y -= 1
                elif y < y1:
                    y += 1

        print(f"The answer is {count} for {input_file}!")
