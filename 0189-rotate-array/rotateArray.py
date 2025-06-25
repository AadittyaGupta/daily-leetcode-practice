class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotations = k % n

        # for _ in range (0,rotations):
        #     e = nums.pop()
        #     nums.insert(0,e)

        nums[:] = nums[n-rotations:] + nums[:n-rotations] 