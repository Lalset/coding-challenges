# LeetCode Mode:

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        p1, p2 = 1, 2
        
        for _ in range(3, n + 1):
            actual = p1 + p2
            p1, p2 = p2, actual
            
        return p2
    
# Local Mode:

# n = int(input("Enter the number of steps: "))

# sol = Solution()
# result = sol.climbStairs(n)

# print("Ways to climb:", result)