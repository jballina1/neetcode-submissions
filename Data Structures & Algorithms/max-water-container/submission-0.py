class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1,p2 = 0, len(heights) - 1
        m = 0
        while p1 < p2:
            m = max(m, (p2 - p1) * min(heights[p1], heights[p2]))
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return m
