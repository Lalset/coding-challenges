#Leet Code Mode:

class Solution:
    def isValidParentheses(self, s: str) -> bool:
        stacks = []
        maps = {')' : '(', '}' : '{', ']' : '['}
        
        for char in s:
            if char in maps:
                last_element = stacks.pop() if stacks else "*"
                if maps[char] != last_element:
                    return False
            else:
                stacks.append(char)
        
        return not stacks
    
# Local Mode:
# s = input("Enter the parentheses string: ")
# sol = Solution()
# print(sol.isValidParentheses(s))