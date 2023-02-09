class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        maxx = num
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if int(nums[i]) < int(nums[j]):
                    
                    nums[j], nums[i] = nums[i] , nums[j]  
                    ans = "".join(nums)
                    maxx = max(maxx,int(ans))
                    nums[j], nums[i] = nums[i] , nums[j]  
                    
        return maxx