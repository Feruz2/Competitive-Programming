class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(k):
            s = defaultdict(int)
            l = 0
            ans = 0
            for i in range(len(nums)):
                s[nums[i]] += 1
                while len(s) > k:
                    s[nums[l]] -= 1
                    
                    if s[nums[l]] == 0:
                        del s[nums[l]]
                        
                    l += 1
                ans += (i - l + 1)
            return ans
        return count(k) - count(k-1)