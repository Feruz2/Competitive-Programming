class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            l = 0
            r = len(ans) - 1
            best = -1
            while l <= r:
                mid = (l + r)// 2
                if ans[mid] >= nums[i]:
                    best = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            if best == -1: 
                ans.append(nums[i])
            else:
                
                ans[best] = nums[i]
            
                
        return len(ans)
                