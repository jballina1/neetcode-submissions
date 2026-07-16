class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasher = {}
        for num in nums:
            if num in hasher:
                hasher[num] += 1
            else:
                hasher[num] = 1
        buckets = [[]]
        for i in range(len(nums)):
            buckets.append([])
        for num, count in hasher.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

