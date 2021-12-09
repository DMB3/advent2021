import common


def get_differences(potential, other):
    return len(potential - other), len(other - potential)


if __name__ == "__main__":
    for input_file in common.inputs:
        digits = {}
        digits_by_length = {}
        total_sum = 0

        for line in common.read_file(input_file):
            signal_patterns, output_value = line.split("|")
            signal_patterns, output_value = signal_patterns.strip(), output_value.strip()

            uniques = []
            for part in output_value.split(" ") + signal_patterns.split(" "):
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

            for potential in digits_by_length[5] + digits_by_length[6]:
                with_8 = get_differences(potential, digits[8]) if 8 in digits else None
                with_4 = get_differences(potential, digits[4]) if 4 in digits else None
                with_7 = get_differences(potential, digits[7]) if 7 in digits else None
                with_1 = get_differences(potential, digits[1]) if 1 in digits else None

                if with_8 == (0, 1) and with_7 == (3, 0) and with_4 == (3, 1) and with_1 == (4, 0):
                    if digits.get(0, None) is not None and digits[0] != potential:
                        # print("0 is repeated!")
                        del (digits[0])
                    else:
                        digits[0] = potential
                        digits_by_length[6] = list(
                            filter(lambda x: x != potential, digits_by_length[6]))
                elif with_8 == (0, 2) and with_7 == (3, 1) and with_4 == (3, 2) and with_1 == (
                        4, 1):
                    if digits.get(2, None) is not None and digits[2] != potential:
                        # print("2 is repeated!")
                        del (digits[2])
                    else:
                        digits[2] = potential
                        digits_by_length[5] = list(
                            filter(lambda x: x != potential, digits_by_length[5]))
                elif with_8 == (0, 2) and with_7 == (2, 0) and with_4 == (2, 1) and with_1 == (
                        3, 0):
                    if digits.get(3, None) is not None and digits[3] != potential:
                        # print("3 is repeated!")
                        del (digits[3])
                    else:
                        digits[3] = potential
                        digits_by_length[5] = list(
                            filter(lambda x: x != potential, digits_by_length[5]))
                elif with_8 == (0, 2) and with_7 == (3, 1) and with_4 == (2, 1) and with_1 == (
                        4, 1):
                    if digits.get(5, None) is not None and digits[5] != potential:
                        # print("5 is repeated!")
                        del (digits[5])
                    else:
                        digits[5] = potential
                        digits_by_length[5] = list(
                            filter(lambda x: x != potential, digits_by_length[5]))
                elif with_8 == (0, 1) and with_7 == (4, 1) and with_4 == (3, 1) and with_1 == (
                        5, 1):
                    if digits.get(6, None) is not None and digits[6] != potential:
                        # print("6 is repeated!")
                        del (digits[6])
                    else:
                        digits[6] = potential
                        digits_by_length[6] = list(
                            filter(lambda x: x != potential, digits_by_length[6]))
                elif with_8 == (0, 1) and with_7 == (3, 0) and with_4 == (2, 0) and with_1 == (
                        4, 0):
                    if digits.get(9, None) is not None and digits[9] != potential:
                        # print("9 is repeated!")
                        del (digits[9])
                    else:
                        digits[9] = potential
                        digits_by_length[6] = list(
                            filter(lambda x: x != potential, digits_by_length[6]))

            output_digits = ""
            for output_digit in output_value.split(" "):
                output_digit = "".join(sorted(output_digit))

                for digit in digits:
                    sorted_digit = "".join(sorted(list(digits[digit])))
                    if sorted_digit == output_digit:
                        output_digits += str(digit)

            total_sum += int(output_digits)

        print(f"Total sum for {input_file} is {total_sum}")
