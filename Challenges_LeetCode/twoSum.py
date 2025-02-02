from typing import List
# LeetCode(
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        
        for i, num in enumerate(nums):
            comp = target - num
            
            if comp in num_dic:
                return[num_dic[comp], i]
            
            num_dic[num] = i        
# )            


# Local Mode (Uncomment this section for local test)
#solution = Solution()

#nums_input = input("Enter numbers (separated by space): ")
#target_input = int(input("Enter the target: "))

#nums = list(map(int, nums_input.split()))
#target = target_input

#result= solution.twoSum(nums,target)
#print(f"Result: {result}")
