class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dicit = defaultdict(int)
        ans = 0
        for i in range(len(s)):
            dicit[s[i]] += 1
            while dicit[s[i]] > 1:
                dicit[s[l]] -= 1
                l += 1
            ans = max(ans,(i - l) + 1)
        return ans