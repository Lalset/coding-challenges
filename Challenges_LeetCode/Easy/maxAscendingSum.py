from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sum += nums[i]
            else:
                max_sum = max(max_sum, sum)
                sum = nums[i]

        return max(max_sum, sum)
    
#Local Mode:
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    sol = Solution()
    print("Result: ", sol.maxAscendingSum(nums))    