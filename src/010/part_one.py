import common

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

MATCHES = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

if __name__ == "__main__":
    for input_file in common.inputs:
        total_score = 0

        for line in common.read_file(input_file):
            expected = []

            for character in line:
                if character in MATCHES.keys():
                    expected.append(MATCHES[character])
                elif character in SCORES.keys():
                    expectation = expected.pop()
                    if expectation == character:
                        continue
                    else:
                        score = SCORES[character]
                        total_score += score
                        break

        print(f"Total score is {total_score} for {input_file}!")
