class Solution:
    def clearDigits(self, s: str) -> str:
        stacks = []
        
        for char in s:
            if char.isdigit():
                if stacks:
                    stacks.pop()
            else:
                stacks.append(char)
        
        return "".join(stacks)
    
# Local Mode:
# s = input("Enter a string: ")
# sol = Solution()
# print(sol.clearDigits(s))
