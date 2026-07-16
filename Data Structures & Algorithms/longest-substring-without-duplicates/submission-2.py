class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        p1, p2 = 0, 1
        ret = 1
        d = {s[p1] : 1}

        while p2 < len(s):
            while s[p2] in d:
                del d[s[p1]]
                p1 += 1

            d[s[p2]] = 1
            ret = max(ret, len(d))
            p2 += 1

        return ret