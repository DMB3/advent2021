import common

digit_1 = "cf"
digit_7 = "acf"
digit_4 = "bcdf"
digit_2 = "acdeg"
digit_3 = "acdfg"
digit_5 = "abdfg"
digit_0 = "abcefg"
digit_6 = "abdefg"
digit_9 = "abcdfg"
digit_8 = "abcdefg"

if __name__ == "__main__":
    for input_file in common.inputs:
        digits = {}
        digits_by_length = {}

        for line in common.read_file(input_file):
            signal_patterns, output_value = line.split("|")
            signal_patterns, output_value = signal_patterns.strip(), output_value.strip()

            uniques = []
            for part in output_value.split(" "):
                uniques.append(part)

            for unique in uniques:
                length = len(unique)
                unique = set(unique)

                if length == 2:
                    digits[1] = unique
                elif length == 3:
                    digits[7] = unique
                elif length == 4:
                    digits[4] = unique
                elif length == 5:
                    # this is either 2, 3 or 5
                    if length not in digits_by_length:
                        digits_by_length[length] = []
                    digits_by_length[length].append(unique)
                elif length == 6:
                    # this is either 0, 6 or 9
                    if length not in digits_by_length:
                        digits_by_length[length] = []
                    digits_by_length[length].append(unique)
                elif length == 7:
                    digits[8] = unique

        print("By digit...")
        for digit in digits:
            print(f"\t{digit} - {digits[digit]}")

        print("By length...")
        for length in digits_by_length:
            print(f"\t{length} - {digits_by_length[length]}")
        break
