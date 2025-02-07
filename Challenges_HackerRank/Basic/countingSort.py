# HackerRank Mode: 
import os

def countingSort(arr):
    counter = [0] * 100
    
    for num in arr:
        counter[num] += 1
        
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
# Local Mode:

# n = int(input("Enter how many numbers: ").strip())
# arr = list(map(int, input("Enter numbers separated by space: ").split()))

# result = countingSort(arr)
# print(" ".join(map(str, result)))