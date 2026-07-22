class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        result = nums[0]
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            result = max(result, curSum)
        return result