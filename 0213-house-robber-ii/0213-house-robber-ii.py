class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        def rec(idx, summ, arr, dp):
            
            if idx in dp:
                return dp[idx]
            
            if idx == len(arr) - 1:
                return arr[idx]
            
            if idx >=  len(arr):
                return 0
            
            ans = 0
            for i in range(idx + 2, len(arr)):
                summ += arr[i]
                ans = max(ans, rec(i, summ, arr, dp))
                summ -= arr[i]
            dp[idx]  = ans + arr[idx]
            return dp[idx]
        
        with_zero_index = rec(0, 0, nums[:-1], defaultdict())
        with_one_index = rec(1, 0, nums, defaultdict())
        with_zero_last = rec(0, 0, nums[1:], defaultdict())
        with_one_last = rec(1, 0, nums[1:], defaultdict())
        # print(with_zero_index, with_one_index, with_zero_last, with_one_last)
        return max(with_zero_index, with_one_index, with_zero_last, with_one_last)