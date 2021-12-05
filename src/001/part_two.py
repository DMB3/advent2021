import common

if __name__ == "__main__":
    for input_file in common.inputs:
        previous = None
        window = []
        increases = 0

        for line in common.read_file(input_file):
            depth = int(line.strip())
            window.append(depth)

            if len(window) == 3:
                total = sum(window)

                if previous is not None and total > previous:
                    increases += 1

                previous = total
                del window[0]

        print(f"There is a total of {increases} increases in {input_file}!")
