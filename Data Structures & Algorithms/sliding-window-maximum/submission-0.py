class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        L,R = 0, k - 1
        while R < len(nums):
            curr_arr = nums[L:R+1]
            max_n = -10000
            for ele in curr_arr:
                max_n = max(ele,max_n)
            result.append(max_n)
            R += 1
            L += 1
        return result