
# HackerRank Mode:

import os

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
            
    return "YES"
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()

# Local Mode:
# if __name__ == '__main__':
#     q = int(input("Enter the number of test cases: ").strip())

#     for q_itr in range(q):
#         n, k = map(int, input("Enter the array size and minimum value k: ").split())
        
#         A = list(map(int, input("Enter the elements of array A: ").split()))
#         B = list(map(int, input("Digite os elementos do array B: ").split()))

#         result = twoArrays(k, A, B)
#         print(result)