import common

if __name__ == "__main__":
    for input_file in common.inputs:
        previous = None
        increases = 0

        for line in common.read_file(input_file):
            depth = int(line.strip())

            if previous is not None and depth > previous:
                increases += 1

            previous = depth

        print(f"There is a total of {increases} increases in {input_file}!")
