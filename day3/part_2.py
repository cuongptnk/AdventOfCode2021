def gamma(binaries, index):
    if len(binaries) == 1 or index >= len(binaries[0]):
        return binaries
    fre = {
        '0': 0,
        '1': 0
    }
    for b in binaries:
        fre[b[index]] += 1
    new_list = []
    if fre['0'] > fre['1']:
        chosen = '0'
    else:
        chosen = '1'
    for b in binaries:
        if b[index] == chosen:
            new_list.append(b)
    return gamma(new_list, index+1)


def epsilon(binaries, index):
    if len(binaries) == 1 or index >= len(binaries[0]):
        return binaries
    fre = {
        '0': 0,
        '1': 0
    }
    for b in binaries:
        fre[b[index]] += 1
    new_list = []
    if fre['0'] > fre['1']:
        chosen = '1'
    else:
        chosen = '0'
    for b in binaries:
        if b[index] == chosen:
            new_list.append(b)
    return epsilon(new_list, index+1)


def solution(binaries):
    gamma_v = gamma(binaries, 0)[0]
    epsilon_v = epsilon(binaries, 0)[0]
    return int(gamma_v, 2) * int(epsilon_v, 2)


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    binaries = []
    with open(input_file, 'r') as f:
        for line in f:
            binaries.append(line.strip())
    print(solution(binaries))


