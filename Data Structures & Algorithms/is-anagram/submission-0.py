class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in hash_t:
                hash_t[t[j]] = 1
            else:
                hash_t[t[j]] += 1
        return hash_s == hash_t
        