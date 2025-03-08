# HackerRank Mode:

import os

def balancedSums(arr):
    total_sum = sum(arr)
    sum_left = 0
    
    for num in arr:
        sum_right = total_sum - sum_left - num
        if sum_left == sum_right:
            return "YES"
        sum_left += num
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
