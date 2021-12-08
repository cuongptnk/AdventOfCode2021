
def solution():
    pass


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    unique_length = [2, 4, 3, 7]

    count = 0
    with open(input_file, 'r') as f:
        for line in f:
            line = line.split('|')
            digits = line[1].strip().split()
            for d in digits:
                if len(d) in unique_length:
                    count += 1
    print(count)
  
