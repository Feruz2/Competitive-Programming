class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        cnt  = 0
        k -= 1
        ans = float('inf')
        for i in range(len(blocks)):
            
            if blocks[i] == "W":
                cnt += 1
                
                
            if i - left == k:
                ans = min(ans,cnt)
                cnt -=  1 if blocks[left] == "W" else 0
                left += 1
                
                    
        return ans