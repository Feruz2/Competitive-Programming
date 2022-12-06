class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            ori = i
            idx = i
            if  i == len(nums) - 1: return True
            
            for j in range(i+1, i + nums[i] + 1):
                
                if j+nums[j]  >= len(nums) - 1:
                    return True
                
                if idx <= j + nums[j] : 
                    i = j
                    idx = j + nums[j]
            if ori == i : return False
            
        return True