# HackerRank Mode:

import os

def superDigit(n, k):
    def get_super_digit(x):
        if len(x) == 1:
            return int(x)
        return get_super_digit(str(sum(int(digit) for digit in x)))

    initial_sum = sum(int(digit) for digit in n) * k
    return get_super_digit(str(initial_sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
