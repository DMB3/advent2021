import collections

import common


def apply_rules(template, rules):
    new_template = template

    index = 1
    while True:
        if index >= len(new_template):
            break

        rule = new_template[index - 1] + new_template[index]

        if rule in rules:
            new_template = new_template[:index] + rules[rule] + new_template[index:]
            index += 2

    return new_template


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

        commons = None
        for x in range(10):
            template = apply_rules(template, rules)
            commons = collections.Counter(template).most_common()

        if commons is None:
            raise ValueError("OMG!")

        result = commons[0][1] - commons[-1][1]
        print(f"Result is {result} for {input_file}")
