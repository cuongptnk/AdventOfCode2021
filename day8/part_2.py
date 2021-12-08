#       0
#   ----------
#   |        |
# 1 |        | 2
#   |    3   |
#   ----------
#   |        |
# 4 |        | 5
#   |    6   |
#   ----------

def solution(line):
    line = line.strip().split('|')
    digits = line[0].split()
    output_value = line[1].strip().split()

    for i, d in enumerate(digits):
        digits[i] = set(d)

    # this will match the digit to set of characters
    digit_to_chrs = {}
    for d in digits:
        key = None
        if len(d) == 2:
            key = 1
        elif len(d) == 4:
            key = 4
        elif len(d) == 3:
            key = 7
        elif len(d) == 7:
            key = 8
        if key is not None:
            digit_to_chrs[key] = d

    # Refer to the image at the top
    # this will match the position index to one character
    pos_to_chr = {}
    # this matches the digit to a set of position indexes
    digit_to_pos = {
        0: set([0, 2, 5, 6, 4, 1]),
        1: set([2, 5]),
        2: set([0, 2, 3, 4, 6]),
        3: set([0, 2, 3, 5, 6]),
        4: set([1, 2, 3, 5]),
        5: set([0, 1, 3, 5, 6]),
        6: set([0, 1, 3, 4, 5, 6]),
        7: set([0, 2, 5]),
        8: set([0, 1, 2, 3, 4, 5, 6]),
        9: set([0, 1, 2, 3, 5, 6])
    }

    # from digit 7 and 1, we know pos 0 is which character
    pos_to_chr[0] = list(digit_to_chrs[7] - digit_to_chrs[1])[0]

    # pos 2 and 5 will match with these 2 characters
    group_2_5 = list(digit_to_chrs[1])
    # pos 1 and 3 will match with these 2 characters
    group_1_3 = list(digit_to_chrs[4] - set(group_2_5))
    # pos 4 and 6 will match with these 2 characters
    group_4_6 = list(digit_to_chrs[8] - set([pos_to_chr[0]]) - set(group_1_3) - set(group_2_5))

    # now try 8 combinations to find the only valid one
    for i in range(2):
        for j in range(2):
            for z in range(2):
                pos_to_chr[2] = group_2_5[i]
                pos_to_chr[5] = group_2_5[1-i]
                pos_to_chr[1] = group_1_3[j]
                pos_to_chr[3] = group_1_3[1-j]
                pos_to_chr[4] = group_4_6[z]
                pos_to_chr[6] = group_4_6[1-z]

                is_valid = True
                for d in digit_to_pos:
                    if d not in [1, 4, 7, 8]:
                        # build set of characters
                        temp = set()
                        for p in digit_to_pos[d]:
                            temp.add(pos_to_chr[p])
                        # check to see if this set is valid
                        if temp not in digits:
                            is_valid = False
                if is_valid:
                    # map each character to a pos:
                    chr_to_pos = {}
                    for k in pos_to_chr:
                        chr_to_pos[pos_to_chr[k]] = k
                    # map set of positions to digit:
                    pos_to_digit = {}
                    for k in digit_to_pos:
                        pos_to_digit[str(digit_to_pos[k])] = k
                    # compute output
                    result = ''
                    for group in output_value:
                        set_pos = set()
                        for c in group:
                            set_pos.add(chr_to_pos[c])
                        result += str(pos_to_digit[str(set_pos)])
                    return int(result)


if __name__ == "__main__":
    # input_file = 'input_sample.txt'
    input_file = 'input_full.txt'

    with open(input_file, 'r') as f:
        total = 0
        for line in f:
            total += solution(line)

    print(total)
  
