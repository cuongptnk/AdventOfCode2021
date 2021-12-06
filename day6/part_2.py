MEMOIZATION = {}
BASE_DAYS = 100


def solution(fish_list):
    # Observe that each fish is independent of others, so we only depend on value => fre count
    # for examle, from full input, we get {'1': 198, '3': 20, '4': 28, '5': 29, '2': 25}
    fre = {}
    for v in fish_list:
        if v not in fre:
            fre[v] = 1
        else:
            fre[v] += 1
    # observer that brute_force_solution is fast for up to 100 days, we will compute 100 days as the base
    compute_base()
    # compute formular(i, 256) for all possible value i
    v_dict = {}
    for i in range(9):
        v_dict[i] = formular(i, 256)
    # result
    total = 0
    for k in fre.keys():
        total += fre[k] * v_dict[k]
    return total


def compute_base():
    # fill in 100 days
    for i in range(9):
        MEMOIZATION[(i, BASE_DAYS)] = brute_force_solution([i], BASE_DAYS)


def brute_force_solution(fish_list, days):
    for _ in range(days):
        count = 0
        for i, f in enumerate(fish_list):
            if f == 0:
                fish_list[i] = 6
                count += 1
            else:
                fish_list[i] -= 1
        for _ in range(count):
            fish_list.append(8)
    return len(fish_list)


def formular(value, days):
    """
    :param value: 0 to 8
    :param days: number of days
    :return:
    """
    if (value, days) in MEMOIZATION:
        return MEMOIZATION[(value, days)]
    if value > 0:
        MEMOIZATION[(value, days)] = formular(value - 1, days - 1)
    else:
        MEMOIZATION[(value, days)] = formular(6, days - 1) + formular(8, days - 1)
    return MEMOIZATION[(value, days)]


if __name__ == "__main__":
    input_file = 'input_sample.txt'
    # input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        for line in f:
            print(solution(list(map(int, line.strip().split(',')))))

