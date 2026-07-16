class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        L, R = 0,0
        s_map = {}
        found = False
        result = "0" * len(s)
        
        while R < len(s):
            check = False
            c = s[R]
            s_map[c] = s_map.get(c,0) + 1
            check = self.contained(t_map, s_map)
            while check:
                if (R-L) < len(result):
                    result = s[L:R+1]
                    found = True
                s_map[s[L]] -= 1
                if s_map[s[L]] == 0:
                    del s_map[s[L]]
                L += 1
                check = self.contained(t_map, s_map)
            R += 1
        if not found:
            return ""
        return result

                

    def contained(self, small, large):
        for k in small:
            if k not in large.keys():
                return False
            else:
                if small[k] > large[k]:
                    return False
        return True
                


            