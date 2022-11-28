class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ans = [1] * len(nums)
        dicit = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                
                if nums[i] > nums[j] and ans[j] + 1 > ans[i]:
                    ans[i] = 1 + ans[j]
                    dicit[i] = dicit[j]
                elif nums[i] > nums[j] and ans[j] + 1 == ans[i]: 
                    dicit[i] += dicit[j] 
                
        maxx = max(ans)
        final = 0
        # print(ans,dicit)
        for i in range(len(ans)):
            if ans[i] == maxx:
                final += dicit[i]
        return final