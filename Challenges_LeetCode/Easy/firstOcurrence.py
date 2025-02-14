# LeetCode Mode:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1): 
            if haystack[i:i+m] == needle:  
                return i  
        
        return -1  

# Local Mode:
haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")

sol = Solution()
print("First occurrence index:", sol.strStr(haystack, needle))  
