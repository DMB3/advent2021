import os

inputs = ["example_input.txt", "real_input.txt"]

if __name__ == "__main__":
    for input_file in inputs:
        file_name = os.path.join("inputs", input_file)
        with open(file_name, "r") as fin:
            x, depth = 0, 0

            for line in fin.readlines():
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
