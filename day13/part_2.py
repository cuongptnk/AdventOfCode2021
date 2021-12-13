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
    return [list(map(int, e.strip('[').strip(']').split(','))) for e in above]


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
    return [list(map(int, e.strip('[').strip(']').split(','))) for e in left]


def print_dots(dots):
    min_x = min([d[0] for d in dots])
    max_x = max([d[0] for d in dots])

    min_y = min([d[1] for d in dots])
    max_y = max([d[1] for d in dots])

    d_set = set()
    for d in dots:
        d_set.add(str(d))

    for y in range(min_y, max_y + 1, 1):
        for x in range(min_x, max_x + 1, 1):
            if str([x, y]) in d_set:
                print('#', end='')
            else:
                print('.', end='')
        print()


def solution(dots, folds):
    for fold in folds:
        if fold[0] == 'y':
            dots = fold_y(dots, int(fold[1]))
        else:
            dots = fold_x(dots, int(fold[1]))
    print_dots(dots)


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
        solution(dots, folds)

