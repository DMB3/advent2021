import common


class Lanternfish:
    def __init__(self, internal_timer=8):
        self.internal_timer = internal_timer

    def step(self):
        self.internal_timer -= 1
        return_value = self.internal_timer < 0

        if return_value:
            self.internal_timer = 6

        return return_value

    def __repr__(self):
        return "%d" % (self.internal_timer,)


if __name__ == "__main__":
    for input_file in common.inputs:
        lanternfishes = None

        for line in common.read_file(input_file):
            lanternfishes = line.split(",")

        fishes = []
        for fish_reset in lanternfishes:
            fishes.append(Lanternfish(internal_timer=int(fish_reset)))

        for days in range(80):
            new_fishes = []
            for lanternfish in fishes:
                if lanternfish.step():
                    new_fishes.append(Lanternfish())

            fishes += new_fishes

        print(f"{days + 1} days have passed and we now have {len(fishes)} fishes...")
