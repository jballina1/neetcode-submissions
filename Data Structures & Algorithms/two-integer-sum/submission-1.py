class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in d:
                return [d[comp],i]
            else:
                d[nums[i]] = i
        