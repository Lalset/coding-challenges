# HackerRank Mode: 
import os

def countingSort(arr):
    counter = [0] * 100
    
    for num in arr:
        counter[num] += 1
        
    return counter
    
# Local Mode:
# if __name__ == '__main__':
#     n = int(input("Enter how many numbers: "))
#     arr = list(map(int, input("Enter numbers separated by space: ").split()))

#     result = countingSort(arr)
#     print(" ".join(map(str, result)))