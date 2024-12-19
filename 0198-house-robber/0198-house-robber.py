class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
#         dp = defaultdict()
#         def rec(idx, summ):
            
#             if idx in dp:
#                 return dp[idx]
            
#             if idx == 0:
#                 return nums[idx]
            
#             if idx < 0:
#                 return 0 
            
            
#             ans = max(rec(idx - 2, summ) + nums[idx] , rec(idx - 1, summ))
            
#             dp[idx]  = ans
#             return dp[idx]
        
#         return rec(len(nums) - 1,0)


        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            not_take = dp[i - 1]
            take = nums[i]
            if i > 1: take += dp [i - 2]
            dp.append(max(take, not_take))
        return dp[-1]