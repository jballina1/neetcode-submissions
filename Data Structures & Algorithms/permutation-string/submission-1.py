class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if n > len(s2):
            return False
        d1 = {}
        for c in s1:
            d1[c] = d1.get(c, 0) + 1
        d2 = {}
        for c in s2[:n]:
            d2[c] = d2.get(c, 0) + 1
        p1 = 0
        p2 = n - 1
        while p2 < len(s2):
            if d1 == d2:
                return True
            d2[s2[p1]] -= 1
            if d2[s2[p1]] == 0:
                del d2[s2[p1]]
            p1 += 1
            p2 += 1
            if p2 < len(s2):
                d2[s2[p2]] = d2.get(s2[p2], 0) + 1

        return False