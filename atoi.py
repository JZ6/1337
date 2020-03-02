class Solution:
    def myAtoi(self, s: str) -> int:
        
        if len(s) <1:
            return 0
    
        curr_i = 0

        while s[curr_i] == ' ':
            curr_i +=1
            if curr_i >= len(s):
                return 0

        n = s[curr_i] == '-'
        if n or s[curr_i]  == '+' :
            curr_i +=1

        curr_val = 0

        while curr_i < len(s) and s[curr_i] != ' ' and s[curr_i].isnumeric():

            c = s[curr_i]

            curr_val *= 10
            curr_val += ord(c) - 48

            curr_i +=1

        result = -curr_val if n else curr_val

        result = min(result, 2**31 -1)
        result = max(result, -2**31)
        
        return result
