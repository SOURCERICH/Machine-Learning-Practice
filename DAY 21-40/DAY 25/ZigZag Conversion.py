class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        result_rows = ['' for i in range(numRows)]  
        current_row, direction = 0, 1 
        for char in s:
            result_rows[current_row] += char  
            if current_row == 0:
                direction = 1  
            elif current_row == numRows - 1:
                direction = -1  
            current_row += direction  
        return ''.join(result_rows)
    


        
