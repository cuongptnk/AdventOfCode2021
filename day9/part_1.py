
def is_low_points(matrix, i, j, M, N):
    if i > 0 and matrix[i][j] >= matrix[i-1][j]:
        return False
    if i < M-1 and matrix[i][j] >= matrix[i+1][j]:
        return False
    if j > 0 and matrix[i][j] >= matrix[i][j-1]:
        return False
    if j < N-1 and matrix[i][j] >= matrix[i][j+1]:
        return False
    return True


def solution(matrix, M, N):
    sum_risk = 0
    for i in range(M):
        for j in range(N):
            if is_low_points(matrix, i, j, M, N):
                sum_risk += 1 + matrix[i][j]
    return sum_risk


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    matrix = []
    r_index = 0
    N = None
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if r_index == 0:
                N = len(line)
            matrix.append([])
            for c in line:
                matrix[r_index].append(int(c))
            r_index += 1
        print(solution(matrix, r_index, N))
  
