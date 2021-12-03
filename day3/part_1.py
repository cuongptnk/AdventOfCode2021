def solution(binaries):
    fre = []
    for i in range(len(binaries[0])):
        fre.append({
            '0': 0,
            '1': 0
        })
    for b in binaries:
        for i in range(len(b)):
            fre[i][b[i]] += 1
    gamma = ''
    epsilon = ''
    for f in fre:
        if f['0'] > f['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    binaries = []
    with open(input_file, 'r') as f:
        for line in f:
            binaries.append(line.strip())
    print(solution(binaries))


