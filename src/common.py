import os

inputs = [os.path.join("inputs", "example_input.txt"),
          os.path.join("inputs", "real_input.txt")]


def read_file(filename):
    with open(filename, "r") as fin:
        for line in fin.readlines():
            yield line.strip()
