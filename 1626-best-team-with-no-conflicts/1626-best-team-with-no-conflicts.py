class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new = []
        for i in range(len(scores)):
            new.append((scores[i],ages[i]))
            
        new.sort(key = lambda x : (x[1],x[0]))
       
        dp = [score for score, age in new]
        
        for i in range(1, len(new)):
            
            for j in range(i):
                
                if new[i][0] >= new[j][0]:
                    dp[i] = max(dp[i], new[i][0] + dp[j])   
                    
        return max(dp)