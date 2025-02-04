from collections import Counter

def matchingStrings(strings, queries):
    freq = Counter(strings) 
    return [freq[q] for q in queries] 

# Local Mode

# if __name__ == '__main__':
#     strings = input("Enter strings (separated by space): ").split()
#     queries = input("Enter queries (separated by space): ").split()

#     print(matchingStrings(strings, queries))

# HackerRank Mode:

import os
from collections import Counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())
    strings = [input().strip() for _ in range(strings_count)]

    queries_count = int(input().strip())
    queries = [input().strip() for _ in range(queries_count)]

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)) + '\n')
    fptr.close()