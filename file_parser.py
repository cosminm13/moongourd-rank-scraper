from itertools import islice

def parse(filename, target_ranks):
    input_file = open(filename, encoding="utf8")
    lines = input_file.readlines()
    parsed_content = []
    start_line = 0
    for i, line in enumerate(lines):
        if "<tbody>" in line:
            start_line = i
            break
    for line in islice(lines, start_line, start_line + target_ranks * 8):
        parsed_content.append(line)
    return parsed_content
