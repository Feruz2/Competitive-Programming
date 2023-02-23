class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for length in range(1, len(nums)):
            for left in range(0, len(nums) - length):
                right = left + length
                for last in range(left + 1, right):
                    coins = nums[left] * nums[last] * nums[right] + dp[left][last] + dp[last][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        return dp[0][len(nums) - 1]