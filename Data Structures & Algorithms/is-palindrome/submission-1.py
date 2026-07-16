class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c.lower() for c in s if c.isalnum())
        s2 = s1[::-1]
        return s1 == s2