
def fold_y(dots, pos):
    # split half
    above = set()
    below = []
    for d in dots:
        if d[1] <= pos:
            above.add(str(d))
        else:
            below.append(d)
    # transform below
    for d in below:
        new_y = pos - (d[1] - pos)
        if str([d[0], new_y]) not in above:
            above.add(str([d[0], new_y]))
    return len(above)


def fold_x(dots, pos):
    # split half
    left = set()
    right = []
    for d in dots:
        if d[0] <= pos:
            left.add(str(d))
        else:
            right.append(d)
    # transform below
    for d in right:
        new_x = pos - (d[0] - pos)
        if str([new_x, d[1]]) not in left:
            left.add(str([new_x, d[1]]))
    return len(left)


def solution(dots, folds):
    if folds[0][0] == 'y':
        res = fold_y(dots, int(folds[0][1]))
    else:
        res = fold_x(dots, int(folds[0][1]))
    return res


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    dots = []
    folds = []

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if ',' in line:
                dots.append(list(map(int, line.split(','))))
            elif 'fold' in line:
                line = line.split()
                folds.append(line[2].split('='))
        print(solution(dots, folds))
  
