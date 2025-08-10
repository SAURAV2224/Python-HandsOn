def maxProduct(nums):
        cur_pd=1
        max_pd=nums[0]
        for num in nums:
            if cur_pd < 0 and num > cur_pd:
                 cur_pd=1
            cur_pd=cur_pd*num
            if cur_pd > max_pd:
                max_pd = cur_pd
            if cur_pd == 0:
                cur_pd = 1

        return max_pd

print(maxProduct([-3,-1,-1]))