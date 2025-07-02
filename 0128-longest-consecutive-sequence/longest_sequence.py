class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        # max_count = 0

        # for i in range (0,n):
        #     num = nums[i]
        #     count = 1
        #     while num+1 in nums:
        #         count +=1 
        #         num = num+1

        #     max_count = max(max_count, count)

        # return max_count    




        my_set = set()
        for i in range(0,n):
            my_set.add(nums[i])

        longest = 0

        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)

        return longest