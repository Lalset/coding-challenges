# HackerRank Mode: 

import os

def maxMin(k, arr):
    arr.sort()
    min_unfair = float('inf')
    
    for i in range(len(arr) - k + 1):
        unfair = arr[i + k - 1] - arr[i]
        min_unfair = min(min_unfair, unfair)
        
    return min_unfair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
