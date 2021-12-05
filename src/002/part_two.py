import common

if __name__ == "__main__":
    for input_file in common.inputs:
        x, depth, aim = 0, 0, 0

        for line in common.read_file(input_file):
            instruction, amount = line.strip().split(" ")

            if instruction == "forward":
                x += int(amount)
                depth += int(amount) * aim
            elif instruction == "down":
                aim += int(amount)
            elif instruction == "up":
                aim -= int(amount)
            else:
                raise ValueError(f"Unknown instruction: {instruction} for amount {amount}")

        print(f"The value for x*depth is {depth}x{x}={depth * x} in {input_file}!")
