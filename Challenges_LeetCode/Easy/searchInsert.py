# LeetCode Mode

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Local Mode:  
    
# nums = list(map(int, input("Enter a list of numbers separated by space: ").split()))
# target = int(input("Enter the target number: "))

# sol = Solution()
# res = sol.searchInsert(nums, target)

# print(f"Index of target: {res}")