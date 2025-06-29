class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_no = float('-inf')
        total = 0

        for i in range(0,n):
            total = total + nums[i]
            max_no = max(max_no, total)
            if total < 0:
                total = 0

        return max_no        