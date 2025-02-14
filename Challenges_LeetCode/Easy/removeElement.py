# LeetCode Mode:
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for j in range(len(nums)):
            if nums [j] != val:
                nums[i] = nums[j]
                i += 1 
                
        return i
    
# Local Mode:

# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# val = int(input("Enter the value to remove: "))

# sol = Solution()
# r = sol.removeElement(nums, val)

# print(f"Number of remaining elements: {r}")
# print(f"Modified array: {nums[:r]}")