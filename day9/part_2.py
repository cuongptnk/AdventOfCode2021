import queue

def is_low_points(matrix, i, j, M, N):
    if i > 0 and matrix[i][j] >= matrix[i - 1][j]:
        return False
    if i < M - 1 and matrix[i][j] >= matrix[i + 1][j]:
        return False
    if j > 0 and matrix[i][j] >= matrix[i][j - 1]:
        return False
    if j < N - 1 and matrix[i][j] >= matrix[i][j + 1]:
        return False
    return True


def basin_size(matrix, M, N, i, j):
    """
    Given the location i and j of the low point, find it's basin'size
    Assuming that 2 basins do not connect together (there are value 9s to seperate them)
    """
    q = queue.Queue()
    visited = {}
    if i > 0 and matrix[i-1][j] != 9:
        q.put([i-1, j])
        visited[str([i-1, j])] = True
    if i < M - 1 and matrix[i+1][j] != 9:
        q.put([i+1, j])
        visited[str([i+1, j])] = True
    if j > 0 and matrix[i][j-1] != 9:
        q.put([i, j-1])
        visited[str([i, j-1])] = True
    if j < N - 1 and matrix[i][j+1] != 9:
        q.put([i, j+1])
        visited[str([i, j+1])] = True
    while not q.empty():
        current_i, current_j = q.get()

        if current_i > 0 and matrix[current_i - 1][current_j] != 9 and str([current_i - 1, current_j]) not in visited:
            q.put([current_i - 1, current_j])
            visited[str([current_i - 1, current_j])] = True

        if current_i < M - 1 and matrix[current_i + 1][current_j] != 9 and str([current_i + 1, current_j]) not in visited:
            q.put([current_i + 1, current_j])
            visited[str([current_i + 1, current_j])] = True

        if current_j > 0 and matrix[current_i][current_j - 1] != 9 and str([current_i, current_j - 1]) not in visited:
            q.put([current_i, current_j - 1])
            visited[str([current_i, current_j - 1])] = True

        if current_j < N - 1 and matrix[current_i][current_j + 1] != 9 and str([current_i, current_j + 1]) not in visited:
            q.put([current_i, current_j + 1])
            visited[str([current_i, current_j + 1])] = True

    return len(visited.keys())


def solution(matrix, M, N):
    low_points = []
    for i in range(M):
        for j in range(N):
            if is_low_points(matrix, i, j, M, N):
                low_points.append([i, j])
    basin_sizes = []
    for lp_i, lp_j in low_points:
        basin_sizes.append(basin_size(matrix, M, N, lp_i, lp_j))
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


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

