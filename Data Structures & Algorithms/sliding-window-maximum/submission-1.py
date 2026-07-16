
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        L,R = 0, k - 1
        while R < len(nums):
            curr_arr = sorted(nums[L:R+1])
            result.append(curr_arr[-1])
            R += 1
            L += 1
        return result