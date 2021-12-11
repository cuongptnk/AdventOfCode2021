
SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def solution(line):
    s = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            s.append(c)
        else:
            if len(s) < 1:
                return SCORES[c]
            if PAIRS[s.pop()] != c:
                return SCORES[c]
    return 0


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    total = 0
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            total += solution(line)
        print(total)
  
