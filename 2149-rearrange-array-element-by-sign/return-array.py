class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # pos = []
        # neg = []

        # for i in range(0,n):
        #     if nums[i] > 0 :
        #         pos.append(nums[i])
        #     if nums[i] < 0:
        #         neg.append(nums[i]) 

        # for i in range(0,len(pos)):
        #     nums[2*i] = pos[i]
        #     nums[(2*i)+1] = neg[i]

        # return nums            

        expected_res = [0] * n
        posIndex = 0 
        negIndex = 1

        for i in range(0,n):
            if nums[i] >= 0:
                expected_res[posIndex] = nums[i]
                posIndex += 2
            else:
                expected_res[negIndex] = nums[i]
                negIndex += 2     
                 
        return expected_res