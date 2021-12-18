import math

def update(matrix, N, M, visited, dis, min_v):
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and dis[i][j] == min_v:
                visited[i][j] = True
                if j < M - 1 and dis[i][j] + matrix[i][j + 1] < dis[i][j + 1]:
                    dis[i][j + 1] = dis[i][j] + matrix[i][j + 1]
                if i < N - 1 and dis[i][j] + matrix[i + 1][j] < dis[i + 1][j]:
                    dis[i + 1][j] = dis[i][j] + matrix[i + 1][j]
                return

# apply dijkstra's algorithm
def solution(matrix, N, M):
    visited = [[False for j in range(M)] for i in range(N)]
    dis = [[math.inf for j in range(M)] for i in range(N)]
    dis[0][0] = 0
    while not visited[N-1][M-1]:
        min_v = math.inf
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and min_v > dis[i][j]:
                    min_v = dis[i][j]

        update(matrix, N, M, visited, dis, min_v)

    return dis[N-1][M-1]


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    matrix = []
    N = None
    M = None
    count = 0
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                matrix.append([])
                if count == 0:
                    M = len(line)
                for j in range(M):
                    matrix[count].append(int(line[j]))
                count += 1
            else:
                break
        N = count
        print(solution(matrix, N, M))
  
