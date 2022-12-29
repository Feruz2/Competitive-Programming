class Solution:
    def maxJump(self, stones: List[int]) -> int:
        diff = 0
        i = 0
        last = 0
        while i < len(stones):
            if i + 2 < len(stones):
                diff = max(diff,abs(stones[i] - stones[i + 2]))
                last = i
            elif i + 1 < len(stones):
                diff = max(diff,abs(stones[i] - stones[i + 1]))
                last = i
            i += 2
        i = 1
        while i < len(stones):
            if i + 2 < len(stones):
                diff = max(diff,abs(stones[i] - stones[i + 2]))
            
            elif i + 1 < len(stones):
                diff = max(diff,abs(stones[i] - stones[i + 1]))
                
            i += 2   
        return diff
            