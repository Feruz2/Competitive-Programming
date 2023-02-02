class Solution:
    def numberOfWays(self, s: str) -> int:
        
        prefix = [0]*len(s)
        prefix[0] = int(s[0])
        
        for i in range(1,len(s)):
            prefix[i] = int(s[i])+prefix[i-1]
        
        ans=0
        for i in range(1, len(s)-1):
            left = prefix[i-1]
            right = prefix[len(s)-1] - prefix[i]
            if s[i]=='1':
                left = abs(i - left)
                right = abs(len(s) - i - right - 1)
            ans += right * left
        return ans
