class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def rec(idx,s):
            if idx == len(nums):
                return s == target
            return rec(idx + 1, s + nums[idx]) + rec(idx + 1,s - nums[idx])
        return rec(0,0)

    