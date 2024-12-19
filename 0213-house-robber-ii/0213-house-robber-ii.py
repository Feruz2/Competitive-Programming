class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==  1:
            return nums[0]
        
        def bottom_up(arr):
            dp = []
            dp.append(arr[0])
            for i in range(1, len(arr)):
                not_take = dp[i - 1]
                take = arr[i]
                if i > 1: take += dp [i - 2]
                dp.append(max(take, not_take))
            return dp[-1]
        
        return max(bottom_up(nums[:-1]), bottom_up(nums[1:]))
        