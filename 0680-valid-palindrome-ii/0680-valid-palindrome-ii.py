class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        cnt1 = 0
        while l < r:
            if s[l] != s[r]:
                cnt1 += 1
                r -= 1
            else:
                l += 1
                r -= 1
                
        if cnt1 == 1 or cnt1 == 0:
            return True
        l = 0
        r = len(s) - 1
        cnt2 = 0 
        while l < r:
            if s[l] != s[r]:
                cnt2 += 1
                l += 1
            else:
                l += 1
                r -= 1
                
        if cnt2 == 1 or cnt2 == 0:
            return True
        return False
        