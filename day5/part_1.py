N = 1000


def solution(lines):
    diagram = []
    for _ in range(N):
        diagram.append([0 for _ in range(N)])
    for l in lines:
        p1, _, p2 = l.split()
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)+1):
                diagram[x1][j] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                diagram[i][y1] += 1
    count = 0
    for i in range(N):
        for j in range(N):
            if diagram[i][j] > 1:
                count += 1
    return count


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    lines = []
    with open(input_file, 'r') as f:
        for line in f:
            lines.append(line)
        print(solution(lines))