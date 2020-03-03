class Solution(object):
    def isMatch(self, text, pattern):
    
        def match_rec(ti, pi):
            
            if pi >= len(pattern):
                return ti >= len(text) 

            if ti >= len(text):
                return is_next_wild_card(pi) and skip_wild_card(ti, pi)

            current_char = text[ti]
            current_matcher = pattern[pi]

            if current_matcher in (current_char, '.'):

                if is_next_wild_card(pi):
                    return check_next_wild_card(ti, pi) or skip_wild_card(ti, pi)
                
                return check_next_both(ti, pi)

            return is_next_wild_card(pi) and skip_wild_card(ti, pi)
        
        
        cache = {}
        def check_cached(ti, pi):
            
            cache_key = (ti, pi)
            
            if cache_key not in cache:
                cache[cache_key] = match_rec(ti, pi)
                
            return cache[cache_key]
        

        def is_next_wild_card(pi):
            return pi < len(pattern) - 1 and pattern[pi+1] == '*'

        
        def skip_wild_card(ti, pi):
            return check_cached(ti, pi+2)
        
        
        def check_next_both(ti, pi):
            return check_cached(ti+1, pi+1)
        
        
        def check_next_wild_card(ti, pi):
            return check_cached(ti+1, pi)
        

        return match_rec(0, 0)
    

def unpack(d, *args):
    return [d[arg] for arg in args]
        
