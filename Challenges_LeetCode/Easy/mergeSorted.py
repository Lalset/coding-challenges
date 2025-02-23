# LeetCode Mode:

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, s = m - 1, n - 1, m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[s] = nums1[i]
                i -= 1
                
            else:
                nums1[s] = nums2[j]
                j -= 1
            s -= 1

# Local Mode:
            
# nums1 = list(map(int, input("Enter nums1 (with extra 0s): ").split()))
# m = int(input("Enter the number of elements in nums1: "))
# nums2 = list(map(int, input("Enter nums2: ").split()))
# n = int(input("Enter the number of elements in nums2: "))

# sol = Solution()
# sol.merge(nums1, m, nums2, n)

# print("Merged nums:", nums1)