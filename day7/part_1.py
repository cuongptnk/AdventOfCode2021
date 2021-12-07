def total_dis(crabs, pos):
    total = 0
    for c in crabs:
        total += max(pos, c) - min(pos, c)
    return total


def solution(crabs):
    s = set(crabs)
    r = float('inf')
    for p in s:
        p_total = total_dis(crabs, p)
        if p_total < r:
            r = p_total
    return r


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        for line in f:
            line = list(map(int, line.split(',')))
            print(solution(line))
  
