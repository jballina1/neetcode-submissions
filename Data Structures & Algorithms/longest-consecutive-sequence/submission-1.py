class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d = {}
        for n in nums:
            d[n] = d.get(n, 1)
        ret = 1
        for n in nums:
            if n -1 not in d:
                m = 1
                while n + 1 in d:
                    m += 1
                    n += 1
                ret = max(m, ret)
        return ret