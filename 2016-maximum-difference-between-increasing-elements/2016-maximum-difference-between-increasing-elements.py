class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -sys.maxsize
        i = len(nums)-1
        while i >= 0:
            j = i-1
            while j >= 0 and nums[j] < nums[i]:
                diff = nums[i] - nums[j]
                max_diff = max(max_diff, diff)
                j -= 1
            i = j
        if max_diff == -sys.maxsize:
            max_diff = -1
        return max_diff