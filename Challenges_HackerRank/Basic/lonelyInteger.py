import os

def lonelyinteger(a):
    unique = 0
    for num in a:
        unique ^= num
    return unique

if __name__ == '__main__':
#HackerRank Mode:
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
    
# Local Mode:
    # a = list(map(int, input("Enter numbers separated by space: ").split()))
    # print("Unique number:", lonelyinteger(a))