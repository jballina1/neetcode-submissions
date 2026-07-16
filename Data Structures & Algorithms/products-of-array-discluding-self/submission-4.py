class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod_non_0 = 1
        zero_count = 0
        for n in nums:
            prod *= n
            if n != 0:
                prod_non_0 *= n
            else:
                zero_count += 1
        ret = [prod] * len(nums)
        for i in range(len(ret)):
            if nums[i] != 0:
                ret[i] = prod // nums[i]
            else:
                ret[i] = prod_non_0 if zero_count == 1 else 0
        return ret