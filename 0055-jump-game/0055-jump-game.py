class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            jump = nums[i]
            nex = -1
            if i + jump >= len(nums) - 1:
                return True
            for j in range(i+1,i+jump+1):
                if nex == -1:
                    nex = j
                elif j + nums[j] >= nums[nex] + nex:
                    nex = j
            if nex != -1:
                i = nex
            else:
                return False
        return False