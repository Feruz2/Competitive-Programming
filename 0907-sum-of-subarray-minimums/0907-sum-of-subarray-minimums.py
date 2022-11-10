class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        left = 0
        nums = arr
        nums.append(float('-inf'))
        s = [-1]
        for i in range(len(nums)):
            while nums[s[-1]] > nums[i]:
                # print(i)
                mid = s.pop()
                interval = ((mid - s[-1]) * (i-mid)) * nums[mid]
                left += interval
            s.append(i)
        nums.pop()
        return left%MOD