#HackerRank Mode:

import os

def gridChallenge(grid):
    sorted_rows = [sorted(row) for row in grid]

    num_rows = len(sorted_rows)
    num_cols = len(sorted_rows[0])

    for col in range(num_cols):
        for row in range(1, num_rows):
            if sorted_rows[row][col] < sorted_rows[row - 1][col]:  
                return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  

    for _ in range(t):
        n = int(input().strip())

        grid = [input().strip() for _ in range(n)]  

        result = gridChallenge(grid)  

        fptr.write(result + '\n')

    fptr.close()
