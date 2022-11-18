class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(idx,s):
            
            if  s < 0:
                return 0
            
            if idx == 0:
                if (s) % coins[0] == 0:
                    return 1
                
                return 0
            return dfs(idx,s - coins[idx]) + dfs(idx - 1,s)
            
        
        return dfs(len(coins) - 1,amount)