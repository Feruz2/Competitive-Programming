class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            i = 0
            for ch in word:
                if i < len(pref) and ch != pref[i]:
                    break
                elif i < len(pref) and ch == pref[i]: 
                    i += 1
                
            if i == len(pref):
                cnt += 1
                
        return cnt