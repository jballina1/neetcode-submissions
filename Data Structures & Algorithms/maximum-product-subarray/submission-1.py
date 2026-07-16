class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        cmin, cmax = 1 , 1
        for n in nums:
            if n == 0:
                cmin, cmax = 1, 1
            else:
                temp = n * cmax
                cmax = max(cmax * n, n * cmin, n)
                cmin = min(temp, n * cmin, n)
                result = max(result, cmax)
        return result