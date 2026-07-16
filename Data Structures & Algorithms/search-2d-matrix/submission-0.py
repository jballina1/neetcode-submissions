class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # Binary search to find the correct row
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                # Target must be in this row
                return self.binarySearch(matrix[m], target)
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1

        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False