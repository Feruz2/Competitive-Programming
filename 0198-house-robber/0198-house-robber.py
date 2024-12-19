class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        dp = defaultdict()
        def rec(idx, summ):
            
            if idx in dp:
                return dp[idx]
            
            if idx == 0:
                return nums[idx]
            
            if idx < 0:
                return 0 
            
            
            ans = max(rec(idx - 2, summ) + nums[idx] , rec(idx - 1, summ))
            
            dp[idx]  = ans
            return dp[idx]
        
        return rec(len(nums) - 1,0)