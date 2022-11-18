class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def rec(idx,s):
            if idx == 0:
                if nums[idx] == 0 and s == 0:
                    return 2
                # print(s)
                if s - nums[idx] == 0 or s + nums[idx] == 0:
                    return 1
                return 0
            return rec(idx - 1, s - nums[idx]) + rec(idx - 1, s + nums[idx])
        return rec(len(nums)-1,target)