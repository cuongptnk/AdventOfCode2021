import queue


def is_able_to_visit(path, n):
    if n[0].isupper():
        return True
    return n not in path


def solution(adj):
    q = queue.Queue()
    path = ['start']
    q.put(path.copy())
    count = 0
    while not q.empty():
        current_path = q.get()

        for n in adj[current_path[-1]]:
            if n == 'end':
                count += 1
                continue
            if is_able_to_visit(current_path, n):
                new_path = current_path.copy()
                new_path.append(n)
                q.put(new_path)
    return count


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'
    adj = {}
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip().split('-')
            if line[0] not in adj:
                adj[line[0]] = [line[1]]
            else:
                adj[line[0]].append(line[1])
            if line[1] not in adj:
                adj[line[1]] = [line[0]]
            else:
                adj[line[1]].append(line[0])
        print(solution(adj))


  
