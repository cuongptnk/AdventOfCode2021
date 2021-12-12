import queue

def increase(matrix, i, j, flash_set, flash_queue):
    if matrix[i][j] != 9:
        matrix[i][j] += 1
    elif (i, j) not in flash_set:
        flash_set.add((i, j))
        flash_queue.put((i, j))


def one_step(matrix, M, N):
    flash_set = set()  # save a list to flash
    flash_queue = queue.Queue()  # to know which is processed/ which not

    # First loop: increase non-9 + add 9 to mapping
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 9:
                flash_set.add((i, j))
                flash_queue.put((i, j))
            else:
                increase(matrix, i, j, flash_set, flash_queue)
    while not flash_queue.empty():
        i, j = flash_queue.get()
        if i > 0:
            increase(matrix, i - 1, j, flash_set, flash_queue)
            if j > 0:
                increase(matrix, i - 1, j - 1, flash_set, flash_queue)
            if j < N - 1:
                increase(matrix, i - 1, j + 1, flash_set, flash_queue)
        if j > 0:
            increase(matrix, i, j - 1, flash_set, flash_queue)
        if j < N - 1:
            increase(matrix, i, j + 1, flash_set, flash_queue)
        if i < M - 1:
            increase(matrix, i + 1, j, flash_set, flash_queue)
            if j > 0:
                increase(matrix, i + 1, j - 1, flash_set, flash_queue)
            if j < N - 1:
                increase(matrix, i + 1, j + 1, flash_set, flash_queue)

    # flash
    for i, j in flash_set:
        matrix[i][j] = 0
    return len(flash_set)


def solution(matrix, M, N):
    step_number = 1
    while one_step(matrix, M, N) != M * N:
        step_number += 1
    return step_number


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    matrix = []
    r_i = 0
    M = None
    N = None
    with open(input_file, 'r') as f:
        for line in f:
            matrix.append([])
            line = line.strip()
            if r_i == 0:
                N = len(line)
            for v in line:
                matrix[r_i].append(int(v))
            r_i += 1
        M = r_i
        print(solution(matrix, M, N))

