from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        k = 0

        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k       

        # nums[:] = [x for x in nums if x != val]
        # print(nums)