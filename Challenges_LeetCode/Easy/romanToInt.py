# HackerRank Mode: (
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
           'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 
        }
        
        final = 0
        previous_value = 0
        
        for sym in reversed(s):
            value = values[sym]
            
            if value < previous_value:
                final -= value
            else:
                final += value
            
            previous_value = value
            
        return final
    # )
    
    
# Local Mode(Uncomment this part): (
    
# if __name__ == "__main__":
#     roman_num = input("Enter a roman number: ")
#     sol = Solution()
#     result = sol.romanToInt(roman_num) 
#     print("Int number: ", result)

# )