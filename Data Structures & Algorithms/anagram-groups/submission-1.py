class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagram(s1,s2):
            if len(s1) != len(s2):
                return False
            d = {}
            for i in range(0, len(s1)):
                d[s1[i]] = d.get(s1[i], 0) + 1
                d[s2[i]] = d.get(s2[i], 0) - 1
            return all(v == 0 for v in d.values())
        
        ret = [[strs[0]]]
        for i in range(1, len(strs)):
            added = False
            for group in ret:
                if anagram(group[0], strs[i]):
                    group.append(strs[i])
                    added = True
            if not added:
                ret.append([strs[i]])
        return ret
            