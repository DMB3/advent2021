import copy
import os

import common


def find_character_counts(lines):
    counts = {}
    for character_index in range(len(lines[0])):
        counts[character_index] = {}
        for line_index in range(len(lines)):
            line = lines[line_index]
            character = line[character_index]

            if character not in counts[character_index]:
                counts[character_index][character] = 0
            counts[character_index][character] += 1

    return counts


def lines_with(character, index, lines):
    return_value = []

    for line in lines:
        if line[index] == character:
            return_value.append(line)

    return return_value


def find_oxygen_rating(lines):
    lines_to_consider = copy.deepcopy(lines)
    counts = find_character_counts(lines_to_consider)

    for character_index in range(len(lines[0])):
        count_0, count_1 = counts[character_index]['0'], counts[character_index]['1']

        if len(lines_to_consider) == 1:
            return lines_to_consider[0]

        zero_lines = lines_with("0", character_index, lines_to_consider)
        one_lines = lines_with("1", character_index, lines_to_consider)

        if count_0 > count_1:
            lines_to_consider = copy.deepcopy(zero_lines)
        else:
            lines_to_consider = copy.deepcopy(one_lines)

        counts = find_character_counts(lines_to_consider)

    if len(lines_to_consider) > 1:
        raise ValueError("OMG!")

    return lines_to_consider[0]


def find_scrubber_rating(lines):
    lines_to_consider = copy.deepcopy(lines)
    counts = find_character_counts(lines_to_consider)

    for character_index in range(len(lines[0])):
        count_0, count_1 = counts[character_index].get('0', 0), counts[character_index].get('1', 0)

        if len(lines_to_consider) == 1:
            return lines_to_consider[0]

        zero_lines = lines_with("0", character_index, lines_to_consider)
        one_lines = lines_with("1", character_index, lines_to_consider)

        if count_0 > count_1:
            lines_to_consider = copy.deepcopy(one_lines)
        else:
            lines_to_consider = copy.deepcopy(zero_lines)

        counts = find_character_counts(lines_to_consider)

    if len(lines_to_consider) > 1:
        raise ValueError("OMG!")

    return lines_to_consider[0]


if __name__ == "__main__":
    for input_file in common.inputs:
        file_name = os.path.join("inputs", input_file)
        lines = list(common.read_file(input_file))

        oxygen_rating = find_oxygen_rating(lines)
        scrubber_rating = find_scrubber_rating(lines)

        life_support = int(oxygen_rating, 2) * int(scrubber_rating, 2)
        print(f"Life support rating is {life_support} in {input_file}!")
