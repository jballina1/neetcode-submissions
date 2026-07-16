class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for i in range(len(nums)):
            if target - nums[i] in hasher:
                return [hasher[target - nums[i]], i]
            if nums[i] not in hasher:
                hasher[nums[i]] = i
            
        