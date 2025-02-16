# HackerRank Mode:

import os

def pageCount(n, p):
    front = p // 2
    back = (n // 2) - (p // 2)
    
    return min(front, back)

# Local Mode:

# n = int(input("Enter the number of pages (n): ").strip())
# p = int(input("Enter the target page (p): ").strip())

# result = pageCount(n, p)

# print("Minimum number of pages:", result)