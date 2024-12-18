class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rec(idx, summ)
        #     if idx == last:
        #         return summ
        #     if idx > last:
        #         return 0
        #     ans = float('-inf')
        #     for j from idx + 2 -> last
        #         summ += nums[j]
        #         ans = max (ans, rec(j))
        #         summ -= nums[j]
        #     return ans + nums[idx]
        dp = defaultdict()
        def rec(idx, summ):
            
            if idx in dp:
                return dp[idx]
            if idx == len(nums) - 1:
                return nums[idx]
            if idx >=  len(nums):
                return 0
            
            ans = 0
            for i in range(idx + 2, len(nums)):
                summ += nums[i]
                ans = max(ans, rec(i, summ))
                summ -= nums[i]
            dp[idx]  = ans + nums[idx]
            return dp[idx]
        
        return max(rec(0, 0), rec(1,0))