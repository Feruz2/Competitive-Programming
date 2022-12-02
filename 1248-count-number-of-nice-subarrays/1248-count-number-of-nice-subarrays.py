class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count(k):
            s = 0
            l = 0
            ans = 0
            for i in range(len(nums)):
                s += nums[i] % 2
                while s > k:
                    s -= nums[l]%2
                    
                        
                    l += 1
                
                ans += (i - l + 1)
            return ans
        return count(k) - count(k-1)