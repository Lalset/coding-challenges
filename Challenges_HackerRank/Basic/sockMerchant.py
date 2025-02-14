# HackerRank Mode:

import os

def sockMerchant(n, ar):
    colors = {}
    pairs = 0
    
    for sock in ar:
        if sock in colors:
            colors[sock] += 1
        else:
            colors[sock] = 1
            
    for counter in colors.values():
        pairs += counter // 2
        
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
# Local Mode:

# if __name__ == '__main__':
#     n = int(input("Enter the number of socks: ").strip())  
#     sockColors = list(map(int, input("Enter the colors of the socks separated by space: ").split()))  

#     result = sockMerchant(n, sockColors)

#     print("Number of pairs:", result)