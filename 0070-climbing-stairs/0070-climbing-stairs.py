class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0, 1]
        for i in range(1, n + 1):
            nextt = dp[-1] + dp[-2]
            dp.append(nextt)
        return dp[-1]