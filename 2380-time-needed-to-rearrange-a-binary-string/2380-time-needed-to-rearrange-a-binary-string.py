class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        """
        0110101
        1011010
        1101100
        1110100
        1111000
        """
        ans=0
        j=0
        
        
        for i in range(len(s)):
            if s[i] == "1":
                if i != j:
                    ans = max(ans + 1,i - j)
                j += 1
        
        return ans