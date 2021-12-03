import os

inputs = ["example_input.txt", "real_input.txt"]

if __name__ == "__main__":
    for input_file in inputs:
        file_name = os.path.join("inputs", input_file)
        with open(file_name, "r") as fin:
            previous = None
            window = []
            increases = 0

            for line in fin.readlines():
                depth = int(line.strip())
                window.append(depth)

                if len(window) == 3:
                    total = sum(window)

                    if previous is not None and total > previous:
                        increases += 1

                    previous = total
                    del window[0]

            print(f"There is a total of {increases} increases in {input_file}!")
