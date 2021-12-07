def total_dis(crabs, pos):
    total = 0
    for c in crabs:
        d = max(pos, c) - min(pos, c)
        total += d * (d+1) / 2
    return total


def solution(crabs):
    l = min(crabs)
    r = max(crabs)
    result = float('inf')
    for p in range(l, r+1, 1):
        p_total = total_dis(crabs, p)
        if p_total < result:
            result = p_total
    return result


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        for line in f:
            line = list(map(int, line.split(',')))
            # total_dis(line, 5)
            print(solution(line))

