class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        max_f = 0
        L,R = 0,0
        letters = {}
        while R < len(s):
            if s[R] in letters:
                letters[s[R]] += 1
            else:
                letters[s[R]] = 1
            max_f = max(max_f, letters[s[R]])
            while (R- L)+ 1 - max_f > k:
                #move left until valid
                letters[s[L]] -= 1
                L += 1    
            result = max(result, R - L + 1)
            R += 1
        return result
            
            