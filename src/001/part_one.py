import os

inputs = ["example_input.txt", "real_input.txt"]

if __name__ == "__main__":
    for input_file in inputs:
        file_name = os.path.join("inputs", input_file)
        with open(file_name, "r") as fin:
            previous = None
            increases = 0

            for line in fin.readlines():
                depth = int(line.strip())

                if previous is not None and depth > previous:
                    increases += 1

                previous = depth

            print(f"There is a total of {increases} increases in {input_file}!")
