# LeetCode Mode:
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
    
# Local Mode:

# nums = list(map(int, input("Enter numbers separated by space:").split())) 
# sol = Solution()
# r = sol.removeDuplicates(nums)

# print(f"Number of unique elements: {r}")
# print(f"Unique numbers: {nums[:r]}")