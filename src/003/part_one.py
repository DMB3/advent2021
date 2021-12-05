import common

if __name__ == "__main__":
    for input_file in common.inputs:
        lines = list(common.read_file(input_file))

        counts = {}
        gamma_rate = ""
        epsilon_rate = ""
        for character_index in range(len(lines[0])):
            counts[character_index] = {}
            for line_index in range(len(lines)):
                line = lines[line_index]
                character = line[character_index]

                if character not in counts[character_index]:
                    counts[character_index][character] = 0
                counts[character_index][character] += 1

            max_count, max_character = None, None
            for character in counts[character_index]:
                count = counts[character_index][character]

                if max_count is None or count > max_count:
                    max_character = character
                    max_count = count

            min_character = "0" if max_character == "1" else "1"

            gamma_rate += max_character
            epsilon_rate += min_character

        power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
        print(f"Power consumption is {power_consumption} in {input_file}!")
