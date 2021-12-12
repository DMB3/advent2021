import common


class Octopus:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level

        self.__adjacents = None
        self.flashed = False
        self.flash_count = 0

    def __repr__(self):
        return f"{self.level}"

    def __get_at(self, octopi, x, y):
        if 0 <= x < len(octopi[0]) and 0 <= y < len(octopi):
            return octopi[y][x]

        return None

    def adjacents(self, octopi):
        if self.__adjacents is not None:
            return self.__adjacents

        self.__adjacents = []
        left = self.__get_at(octopi, self.x - 1, self.y)
        up_left = self.__get_at(octopi, self.x - 1, self.y - 1)
        down_left = self.__get_at(octopi, self.x - 1, self.y + 1)
        right = self.__get_at(octopi, self.x + 1, self.y)
        up_right = self.__get_at(octopi, self.x + 1, self.y - 1)
        down_right = self.__get_at(octopi, self.x + 1, self.y + 1)
        up = self.__get_at(octopi, self.x, self.y - 1)
        down = self.__get_at(octopi, self.x, self.y + 1)

        for adjacent in (up, down, left, right, up_left, down_left, up_right, down_right):
            if adjacent is not None:
                self.__adjacents.append(adjacent)

        return self.__adjacents

    def increase_level(self, octopi):
        self.level += 1

        if self.level > 9:
            self.flash(octopi)

    def rest(self):
        if self.flashed:
            self.flash_count += 1
            self.level = 0

        self.flashed = False

    def flash(self, octopi):
        if self.flashed:
            return

        if self.level > 9:
            self.flashed = True

            for adjacent in self.adjacents(octopi):
                adjacent.increase_level(octopi)


def print_octopi(octopi):
    line = ""

    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            line = f"{line}{octopi[y][x].level}"

        line = f"{line}\n"

    print(line.strip())


def do_step(octopi):
    for y in octopi:
        for x in octopi[y]:
            octopi[y][x].increase_level(octopi)

    for y in octopi:
        for x in octopi[y]:
            octopi[y][x].rest()


def all_flashed(octopi):
    for y in octopi:
        if any([octopus.level != 0 for octopus in octopi[y].values()]):
            return False

    return True


if __name__ == "__main__":
    for input_file in common.inputs:
        octopi = {}

        y = 0
        for line in common.read_file(input_file):
            octopi[y] = {}
            x = 0

            for energy_level in line:
                octopi[y][x] = Octopus(x, y, int(energy_level))
                x += 1

            y += 1

        step = 1
        while True:
            do_step(octopi)

            if all_flashed(octopi):
                print(f"For {input_file} all otcopi will flash at {step}!")
                break

            step += 1
