# LeetCode Mode:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []

        pascal = [[1]]

        for i in range(1, numRows):
            previous_row = pascal[-1]

            new_row = [1]

            for j in range(len(previous_row) - 1):
                new_row.append(previous_row[j] + previous_row[j + 1])
        	
            new_row.append(1)
            
            pascal.append(new_row)

        return pascal