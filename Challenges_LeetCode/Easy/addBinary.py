# LeetCode Mode:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin (int(a, 2) + int(b, 2))[2:]
    
    
# Local Mode:

# a = input("Enter the first binary num: ")
# b = input("Enter second binary num: ")

# sol = Solution()
# result = sol.addBinary(a, b)

# print("Binary Sum:", result)