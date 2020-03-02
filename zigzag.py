class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows < 2:
            return s
        
        curr_row = 0
        direction = 1
        result = [[] for i in range(numRows)]
        
        for c in s:
            
            result[curr_row].append(c)
            
            curr_row += direction
            
            if curr_row >= numRows-1 or curr_row <= 0:
                direction = -direction
                
            
        joined = map(lambda row: "".join(row), result)
        return "".join(joined)
