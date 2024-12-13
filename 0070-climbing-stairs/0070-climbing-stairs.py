class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = defaultdict()
        def rec(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
                
            dp[n] = rec(n - 1) + rec(n - 2)
            return dp[n]
        
        return rec(n)