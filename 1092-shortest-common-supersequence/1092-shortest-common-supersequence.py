class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = []
        for i in range(len(str1) + 1):
            new = []
            for j in range(len(str2) + 1):
                new.append(0)
            dp.append(new)
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
       
        ans = [""]*((len(str1) + len(str2)) - dp[-1][-1])
        i = len(dp) - 1
        j = len(dp[0])-1
        z = len(ans) - 1
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                
                ans[z] = str1[i - 1]
                z -= 1
                i = i-1
                j = j -1
            elif dp[i-1][j] >= dp[i][j-1]:
                   
                    ans[z] = str1[i - 1]
                    z -= 1
                    i = i - 1
            else:
                
                ans[z] = str2[j - 1]
                z -= 1
                j -= 1
        if j >= 0:
        
            arr = str2[:j]
            arr = arr[::-1]
            for v in arr:
                ans[z] = v
                z -= 1
        if i >= 0:
           
            arr = str1[:i]
            arr =arr[::-1]
            for i in arr:
                ans[z] = i
                z -= 1
        return "". join(ans)
        