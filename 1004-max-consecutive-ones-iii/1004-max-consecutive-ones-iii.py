class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        summ = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                summ += 1
                k -= 1
            summ += nums[i]
            while k < 0:
                if nums[l] == 0:
                    k += 1
                    summ -= 1
                summ -= nums[l]
                l += 1
            ans  =  max(ans,summ)
        return ans
            