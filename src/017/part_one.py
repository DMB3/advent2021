import common


class Probe:
    def __init__(self, target):
        self.__reset()

        self.min_x, self.max_x = target[0]
        self.min_y, self.max_y = target[1]

        if self.min_x > self.max_x:
            self.min_x, self.max_x = self.max_x, self.min_x
        if self.min_y > self.max_y:
            self.min_y, self.max_y = self.max_y, self.min_y

    def __reset(self):
        self.x = 0
        self.y = 0
        self.step_count = 0

    def step(self):
        self.x += self.vx
        self.y += self.vy

        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1

        self.vy -= 1
        self.step_count += 1

    @property
    def in_target(self):
        return (self.min_x <= self.x <= self.max_x) and (self.min_y <= self.y <= self.max_y)

    @property
    def lost_forever(self):
        return self.x > self.max_x or self.y < self.min_y

    def test_velocity(self, velocity):
        self.__reset()
        self.vx, self.vy = velocity
        maximum_y = 0

        while not self.lost_forever:
            maximum_y = max(maximum_y, self.y)

            if self.in_target:
                return True, maximum_y

            self.step()

        return False, maximum_y


if __name__ == "__main__":
    for input_file in common.inputs:
        x, y = 0, 0

        for line in common.read_file(input_file):
            _, targets = line.split(":")
            x_targets, y_targets = targets.split(",")

            probe = Probe(([int(n) for n in x_targets.split("=")[1].split("..")],
                           [int(n) for n in y_targets.split("=")[1].split("..")]))

            best_height = None
            best_coords = None
            for vx in range(-100, 100):
                for vy in range(-100, 100):
                    done, height = probe.test_velocity((vx, vy))

                    if done and (best_height is None or height > best_height):
                        best_height = height
                        best_coods = (vx,vy)

            print(f"The answer {best_height} is reached for {input_file}")
            print(f"\tThe best velocity is {best_coords}")
