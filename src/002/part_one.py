import common

if __name__ == "__main__":
    for input_file in common.inputs:
        x, depth = 0, 0

        for line in common.read_file(input_file):
            instruction, amount = line.strip().split(" ")

            if instruction == "forward":
                x += int(amount)
            elif instruction == "down":
                depth += int(amount)
            elif instruction == "up":
                depth -= int(amount)
            else:
                raise ValueError(f"Unknown instruction: {instruction} for amount {amount}")

        print(f"The value for x*depth is {depth}x{x}={depth * x} in {input_file}!")
