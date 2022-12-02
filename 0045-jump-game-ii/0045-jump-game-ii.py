class Solution:
    def jump(self, nums: List[int]) -> int:

        i = 0
        if i == len(nums) - 1:
            return 0
        cnt = 0
        while i < len(nums):
            jump = nums[i]
            nex = -1
            if i + jump >= len(nums) - 1:
                cnt += 1
                break
            for j in range(i+1,i+jump+1):
                if nex == -1:
                    nex = j
                elif j + nums[j] >= nums[nex] + nex:
                    nex = j
            if nex != -1:
                i = nex
                cnt += 1
        return cnt