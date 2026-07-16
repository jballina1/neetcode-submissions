class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num, count in d.items():
            buckets[count].append(num)
        
        ret = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret