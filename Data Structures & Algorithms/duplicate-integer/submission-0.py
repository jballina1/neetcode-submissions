class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            if num in lookup:
                return True
            else:
                lookup[num] = 0
        return False