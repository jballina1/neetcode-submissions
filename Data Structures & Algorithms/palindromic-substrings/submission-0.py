class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            res += tmp
            tmp = self.helper(s, i, i+1)
            res += tmp
        return res

    def helper(self, s, l, r):
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1; r += 1
        return result