import collections

import common


def get_counts(template):
    single_counts = {}
    char_count = collections.Counter(template).most_common()
    for character, count in char_count:
        single_counts[character] = count

    pair_counts = {}
    for index in range(len(template) - 1):
        pair = template[index] + template[index + 1]
        pair_counts[pair] = pair_counts.get(pair, 0) + 1

    return single_counts, pair_counts


if __name__ == "__main__":
    for input_file in common.inputs:
        seeing_rules = False
        template = None
        rules = {}

        for line in common.read_file(input_file):
            if seeing_rules:
                pair, insertion = line.split("->")
                rules[pair.strip()] = insertion.strip()
            else:
                if line == "":
                    seeing_rules = True
                    continue

                template = line

        if template is None:
            raise ValueError("OMG!")

        single_counts, pair_counts = get_counts(template)
        for x in range(40):
            step_counts = {}

            for key in pair_counts:
                to_add = rules[key]

                first_pair = key[0] + to_add
                second_pair = to_add + key[1]

                step_counts[first_pair] = step_counts.get(first_pair, 0) + pair_counts[key]
                step_counts[second_pair] = step_counts.get(second_pair, 0) + pair_counts[key]

                single_counts[to_add] = single_counts.get(to_add, 0) + pair_counts[key]

            pair_counts = step_counts.copy()

        most_common = single_counts[max(single_counts.keys(), key=(lambda c: single_counts[c]))]
        least_common = single_counts[min(single_counts.keys(), key=(lambda c: single_counts[c]))]

        result = most_common - least_common
        print(f"Result is {result} for {input_file}")
