#HackerRank Mode: 
import os

def diagonalDifference(arr):
    n = len(arr)
    
    left_diag = 0
    right_diag = 0
    
    for i in range(n):
        left_diag += arr[i][i]
        right_diag += arr [i][n - 1 - i]
        
    return abs(left_diag - right_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Local Mode:

# if __name__ == "__main__":
#     n = int(input("Enter the size(rows) of the array: "))  

#     arr = []
#     print("Enter array values row by row: ")  

#     for _ in range(n):
#         arr.append(list(map(int, input().split())))
        
#     print("Diagonal difference:", diagonalDifference(arr))  
