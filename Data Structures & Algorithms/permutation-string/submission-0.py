class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        small = {}
        for i in range(n):
            small[s1[i]] = small.get(s1[i], 0) + 1
        L, R = 0, n-1
        while R < len(s2):
            check = True
            large = {}
            for i in range (L,R+1):
                large[s2[i]] = large.get(s2[i],0) + 1
            for k in large:
                if k not in small.keys():
                    check = False
                    break
                else:
                    if large[k] != small[k]:
                        check = False
                        break
            if check:
                return True
            R += 1
            L += 1
        return False