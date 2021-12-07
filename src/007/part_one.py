import common

if __name__ == "__main__":
    for input_file in common.inputs:
        xs = []
        for line in common.read_file(input_file):
            xs = [int(x) for x in line.split(",")]

        best_so_far = min([sum([abs(x - another_x) for x in xs]) for another_x in range(max(xs))])

        print(f"For {input_file} best alignment will cost {best_so_far}")
