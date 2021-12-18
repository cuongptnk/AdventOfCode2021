
def compose(original, rules):
    result = ''
    for i in range(len(original) - 1):
        result += original[i]
        pair = original[i] + original[i + 1]
        if pair in rules:
            result += rules[pair]
    result += original[-1]

    return result


def solution(original, rules):
    s = original
    for _ in range(10):
        s = compose(s, rules)

    fre = {}
    for c in s:
        if c not in fre:
            fre[c] = 1
        else:
            fre[c] += 1

    fre_list = [fre[k] for k in fre.keys()]
    return max(fre_list) - min(fre_list)


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    count = 0
    original = None
    rules = {}
    with open(input_file, 'r') as f:
        for line in f:
            if count == 0:
                original = line.strip()
            elif count >= 2:
                line = line.strip().split('->')
                rules[line[0].strip()] = line[1].strip()
            count += 1
        print(solution(original, rules))

  
