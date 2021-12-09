import common

digit_0 = "abcefg"
digit_1 = "cf"
digit_2 = "acdeg"
digit_3 = "acdfg"
digit_4 = "bcdf"
digit_5 = "abdfg"
digit_6 = "abdefg"
digit_7 = "acf"
digit_8 = "abcdefg"
digit_9 = "abcdfg"

if __name__ == "__main__":
    for input_file in common.inputs:
        counts = {}

        for line in common.read_file(input_file):
            signal_patterns, output_value = line.split("|")
            signal_patterns, output_value = signal_patterns.strip(), output_value.strip()

            uniques = []
            for part in output_value.split(" "):
                uniques.append(part)

            for unique in uniques:
                unique = len(unique)
                if unique not in counts:
                    counts[unique] = 0

                counts[unique] += 1

        result = counts[len(digit_1)] + counts[len(digit_4)] + counts[len(digit_7)] + counts[len(digit_8)]
        print(f"Count is {result} for {input_file}")
