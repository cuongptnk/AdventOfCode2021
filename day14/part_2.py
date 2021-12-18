# Idea: a dict to count fre of pairs

def dict_increase(d, key, count=1):
    if key not in d:
        d[key] = count
    else:
        d[key] += count


def compose(polymer, rules):
    result = {}
    for pair in polymer.keys():
        new_pair_one = pair[0] + rules[pair]
        new_pair_two = rules[pair] + pair[1]
        dict_increase(result, new_pair_one, polymer[pair])
        dict_increase(result, new_pair_two, polymer[pair])
    return result


def solution(polymer, rules, original):
    for _ in range(40):
        polymer = compose(polymer, rules)

    fre = {}
    for pair in polymer:
        c = pair[0]
        dict_increase(fre, c, polymer[pair])

    c = original[-1]
    dict_increase(fre, c)

    fre_list = [fre[k] for k in fre.keys()]
    return max(fre_list) - min(fre_list)


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    count = 0
    original = None
    polymer = {}
    rules = {}
    with open(input_file, 'r') as f:
        for line in f:
            if count == 0:
                line = line.strip()
                original = line
                for i in range(len(line)-1):
                    if line[i:i+2] not in polymer:
                        polymer[line[i:i+2]] = 1
                    else:
                        polymer[line[i:i + 2]] += 1
            elif count >= 2:
                line = line.strip().split('->')
                rules[line[0].strip()] = line[1].strip()
            count += 1
        print(solution(polymer, rules, original))
