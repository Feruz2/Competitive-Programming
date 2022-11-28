class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        if len(nums) == 5:
            ans = float('inf')
            for i in range(len(nums) - 1):
                ans = min(ans,nums[i + 1] - nums[i])
            return ans
        i = 0
        j = -4
        ans = float('inf')
        k = 0
        while k < 4:
            # print(nums[j] - nums[i],j,i)
            ans = min(ans,nums[j] - nums[i])
            i += 1
            j += 1
            k += 1
        return ans