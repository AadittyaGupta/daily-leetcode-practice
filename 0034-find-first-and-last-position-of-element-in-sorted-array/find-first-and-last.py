from typing import List

class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)
        lb = -1
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb

    def upperBound(self, nums, target):
        n = len(nums)
        ub = -1
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] > target:
                # ub = mid
                high = mid - 1
            else:
                ub = mid
                low = mid + 1

        return ub              

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = self.lowerBound(nums, target)

        if first == -1 or nums[first] != target:
            return [-1,-1]

        last = self.upperBound(nums, target)

        # return [first, last - 1]
        return [first, last]
