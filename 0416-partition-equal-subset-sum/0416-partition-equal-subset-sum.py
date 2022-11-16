class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        dp = []
        for i in range(len(nums)):
            new_row = []
            for j in range(summ + 1):
                new_row.append(False)
            dp.append(new_row)
            
        for i in range(len(nums)):
            dp[i][0] = True
            
        if nums[0] <= summ:
            
            dp[0][nums[0]] = True
        
        for i in range(1,len(nums)):
            for j in range(summ + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]    
            
        return dp[-1][-1]
        