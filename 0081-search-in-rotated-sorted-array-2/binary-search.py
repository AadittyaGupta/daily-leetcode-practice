from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # n = len(nums)
        # for i in range(0,n):
        #     if nums[i] == target:
        #         return True
        # return False    

        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False                
