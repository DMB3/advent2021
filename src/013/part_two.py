import common


class Origami:
    def __init__(self):
        self.dots = {}

        self.__width = None
        self.__height = None

    @property
    def visible_dots(self):
        visible = 0

        for y in self.dots:
            for x in self.dots[y]:
                if self.dots[y][x] == "#":
                    visible += 1

        return visible

    def add(self, x, y, piece="#"):
        if y not in self.dots:
            self.dots[y] = {}

        self.dots[y][x] = piece

    def get_dot_at(self, x, y):
        return self.dots.get(y, {}).get(x, ".")

    def fold_along(self, coordinate, value):
        print("Fold along", coordinate, value)

        if coordinate == "y":
            for y in range(0, value):
                for x in range(0, self.width):
                    original_dot = self.get_dot_at(x, y)
                    replacement_dot = self.get_dot_at(x, self.height - y - 1)

                    if original_dot == "#":
                        continue

                    self.add(x, y, piece=replacement_dot)

            for y in range(value, self.height):
                if y in self.dots:
                    del (self.dots[y])
                    self.__height = None
        elif coordinate == "x":
            for y in range(0, self.height):
                for x in range(0, self.width):
                    original_dot = self.get_dot_at(x, y)
                    replacement_dot = self.get_dot_at(self.width - x - 1, y)

                    if original_dot == "#":
                        continue

                    self.add(x, y, piece=replacement_dot)

            for y in self.dots:
                for x in range(value, self.width):
                    if x in self.dots[y]:
                        del (self.dots[y][x])
                        self.__width = None
        else:
            raise ValueError(f"Unknown coordinate to fold {coordinate}")

    def __repr__(self):
        result = ""

        for y in range(self.height):
            for x in range(self.width):
                result += self.get_dot_at(x, y)
            result += "\n"

        return f"{result} with {self.visible_dots} visible dots"

    @property
    def height(self):
        if self.__height is not None:
            return self.__height

        self.__height = max(y for y in self.dots) + 1
        return self.__height

    @property
    def width(self):
        if self.__width is not None:
            return self.__width

        max_x = 0

        for y in self.dots:
            max_x = max(max_x, max(x for x in self.dots[y]))

        self.__width = max_x + 1 if max_x > 0 else 0
        return self.__width


if __name__ == "__main__":
    for input_file in common.inputs:
        origami = Origami()
        reached_instructions = False

        for line in common.read_file(input_file):
            if reached_instructions:
                coordinate, value = line.split("=")
                coordinate = coordinate[-1]
                origami.fold_along(coordinate, int(value))
                print(f"There are {origami.visible_dots} visible dots for {input_file} after "
                      f"last instruction")
            elif line != "":
                x, y = [int(n) for n in line.split(",")]
                origami.add(x, y)
            else:
                reached_instructions = True

        print(origami)
