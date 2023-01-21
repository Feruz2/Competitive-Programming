class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count(k):
            l = 0
            res = 0
            for i in range(len(nums)):
                k -= (nums[i]%2)
                while k < 0:
                    k += nums[l]%2
                    l += 1
                res += (i-l+1)
            return res
        return count(k) - count(k-1)