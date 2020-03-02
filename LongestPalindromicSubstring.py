class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2:
            
            return s
        
        
        possible_centers = []

        longest =(0,"")

        for i, c in enumerate(s):

            if i < len(s)-1:
                rc = s[i+1]

                if rc ==c:
                    possible_centers.append([i, i+1])

            if i < len(s)-2:
                sc = s[i+2]       
                if sc ==c:
                    possible_centers.append([i, i+2])
                    
        if len(possible_centers) == 0:
            return s[0]


        for center in possible_centers:

            start, end = center

            building = True

            while start > 0 and end < len(s)-1 and building:

                if s[start-1] == s [end+1]:
                    start -= 1
                    end += 1
                else:        
                    building = False


            if end - start > longest[0]:
                longest = (end - start, s[start:end+1])

        return longest[1]
