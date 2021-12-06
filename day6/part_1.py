def solution(fish_list):
    for _ in range(80):
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


if __name__ == "__main__":
    input_file = 'input_sample.txt'
    # input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        for line in f:
            print(solution(list(map(int, line.strip().split(',')))))

