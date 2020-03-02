class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        
        rev = s[::-1]
        
        if '-' == rev[-1]:
            rev = '-' + rev[:-1]
        
        ri = int(rev)
        
        return 0 if abs(ri) > (2**31 -1) else ri
         
