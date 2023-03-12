class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        cur_upper = 0
        cur_lowwer = 0
        count = 0

        for i in range(len(nums)):
            cur_upper = upper - nums[i]
            cur_lower = lower - nums[i]
            """
            lower = 8 cur = 4
            upper = 10 cur = 6
            [0,1,4,4,5,8]    4, 6 
                l = 2
                r = 5
            """
            left = bisect.bisect_left(nums, cur_lower)
            right = bisect.bisect_right(nums, cur_upper)

            count += right-left 
            if left <= i < right:
                count -= 1

        return count//2

                