class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        @cache
        def rec(idx,summ):
            
            if summ == 0:
                
                return True
            
            if idx >= len(nums):
                return False
            
            if summ < 0: return False
            
            return rec(idx + 1, summ - nums[idx]) or rec(idx + 1, summ)        
        
        return rec(0,summ)