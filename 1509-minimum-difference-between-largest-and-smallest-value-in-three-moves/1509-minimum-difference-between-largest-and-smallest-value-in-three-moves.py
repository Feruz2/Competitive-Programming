class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            # cause you can make all the numbers the same
            return 0

        i = 0
        j = -4
        ans = float('inf')
        k = 0
        while k <= 3:
            ans = min(ans,nums[j] - nums[i])
            i += 1
            j += 1
            k += 1
        return ans