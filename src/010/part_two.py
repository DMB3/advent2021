import common

SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

MATCHES = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

if __name__ == "__main__":
    for input_file in common.inputs:
        incomplete_lines = []

        for line in common.read_file(input_file):
            expected = []
            is_invalid = False

            for character in line:
                if character in MATCHES.keys():
                    expected.append(MATCHES[character])
                elif character in SCORES.keys():
                    expectation = expected.pop()
                    if expectation == character:
                        continue
                    else:
                        is_invalid = True
                        continue

                if is_invalid:
                    break

            if not is_invalid and len(expected) > 0:
                incomplete_lines.append((line, expected))

        scores = []
        for line, missing in incomplete_lines:
            line_score = 0
            for piece in missing[::-1]:
                line_score *= 5
                line_score += SCORES[piece]
            scores.append(line_score)

        score = sorted(scores)[int(len(scores) / 2)]
        print(f"Score is {score} for {input_file}")
