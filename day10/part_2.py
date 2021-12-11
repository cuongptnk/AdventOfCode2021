SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def is_invalid(line):
    s = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            s.append(c)
        else:
            if len(s) < 1:
                return True
            if PAIRS[s.pop()] != c:
                return True
    return False

def completion(line):
    result = ''
    s = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            s.append(c)
        else:
            s.pop()
    while len(s):
        result += PAIRS[s.pop()]
    return result


def score(s):
    total = 0
    for c in s:
        total = total * 5 + SCORES[c]
    return total


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    incompletes = []
    scores = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not is_invalid(line):
                incompletes.append(line)
        for line in incompletes:
            scores.append(score(completion(line)))
        scores.sort()
        m = (len(scores)-1)//2
        print(scores[m])

