class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        row1 = int(s[1])
        row2 = int(s[4])
        col1 = ord(s[0]) 
        col2 = ord(s[3]) 
        res = []
        
        for i in range(col1, col2+1):  
            for j in range(row1, row2+1):
                res.append(f"{chr(i)}{j}") 
        return res







