class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicit = defaultdict(int)
        for i in range(len(s)):
            dicit[s[i]] += 1
        for i in range(len(s)):
            if dicit[s[i]] == 1:
                return i
        return -1