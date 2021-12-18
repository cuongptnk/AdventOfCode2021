import math
import heapq


def update(matrix, N, M, visited, dis, i, j, q):
    visited[i][j] = True
    if j < M - 1 and not visited[i][j+1] and dis[i][j] + matrix[i][j + 1] < dis[i][j + 1]:
        dis[i][j + 1] = dis[i][j] + matrix[i][j + 1]
        heapq.heappush(q, (dis[i][j + 1], [i, j+1]))
    if i < N - 1 and not visited[i+1][j] and dis[i][j] + matrix[i + 1][j] < dis[i + 1][j]:
        dis[i + 1][j] = dis[i][j] + matrix[i + 1][j]
        heapq.heappush(q, (dis[i + 1][j], [i+1, j]))
    if i > 0 and not visited[i-1][j] and dis[i][j] + matrix[i-1][j] < dis[i-1][j]:
        dis[i - 1][j] = dis[i][j] + matrix[i-1][j]
        heapq.heappush(q, (dis[i - 1][j], [i-1, j]))
    if j > 0 and not visited[i][j-1] and dis[i][j] + matrix[i][j-1] < dis[i][j-1]:
        dis[i][j-1] = dis[i][j] + matrix[i][j-1]
        heapq.heappush(q, (dis[i][j-1], [i, j-1]))


# apply dijkstra's algorithm with priority heap
def solution(matrix, N, M):
    visited = [[False for j in range(M)] for i in range(N)]
    dis = [[math.inf for j in range(M)] for i in range(N)]
    dis[0][0] = 0
    count = 0
    q = []
    heapq.heappush(q, (0, [0, 0]))
    while not visited[N - 1][M - 1]:
        _, [i, j] = heapq.heappop(q)
        update(matrix, N, M, visited, dis, i, j, q)
        count += 1
        # print(count)
    return dis[N - 1][M - 1]


def generate(matrix, N, M):
    new_matrix = []
    for i in range(5*N):
        new_matrix.append([])
        for j in range(5*M):
            v = matrix[i%N][j%M] + i//N + j//M
            if v > 9:
                v -= 9
            new_matrix[i].append(v)
    return new_matrix


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

        new_matrix = generate(matrix, N, M)
        print(solution(new_matrix, 5*N, 5*M))
        # print(solution(matrix, N, M))

