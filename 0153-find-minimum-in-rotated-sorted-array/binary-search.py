from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n =len(nums)
        low = 0
        high = n - 1
        lowest = float("inf")

        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] <= nums[high]:
                lowest = min(lowest, nums[mid])
                high = mid - 1
            else:
                lowest = min(lowest, nums[mid])
                low = mid + 1
        return lowest        
