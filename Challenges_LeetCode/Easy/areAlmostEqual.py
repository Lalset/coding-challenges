# LeetCode Mode(

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        notEqual = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                notEqual.append(i)

        
        if len(notEqual) == 2:
            i, j = notEqual
            return s1[i] == s2[j] and s1[j] == s2[i]

        return False 
    #     ) 
    
    
# if __name__ == "__main__":
    
#     s1 = input("Enter first string: ").strip()
#     s2 = input("Enter second string ").strip()
    
    
#     sol = Solution()
    
#     result = sol.areAlmostEqual(s1, s2)
#     print(result)
    