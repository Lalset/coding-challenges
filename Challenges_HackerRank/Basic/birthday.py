#HackerRank Mode:This was a little difficult!

import os

#Function:
def birthday(s, d, m):
    count = 0
    curr_sum = sum(s[:m])
    
    if curr_sum == d:
        count +=1
        
    for i in range(len(s) - m):
        curr_sum = curr_sum - s[i] + s[i + m]
        if curr_sum == d:
            count += 1
            
    return count
# HackerRank Input:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

# Local Mode

# if __name__ == '__main__':
#     n = int(input("Enter the size of the chocolate bar: "))
#     s = list(map(int, input("Enter the numbers on the chocolate bar: ").split()))
#     d, m = map(int, input("Enter Ron's birthday (day/month): ").split())
    
#     result = birthday(s, d, m)
#     print("Number of ways to divide the chocolate:", result)