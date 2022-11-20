#User function Template for python3
from collections import defaultdict
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        # dp = defaultdict(int)
        # def rec(idx,left):
        #     if (idx,left) in dp:
        #         return dp[(idx,left)]
        #     if left < 0:
        #         return float('-inf')
        #     if idx == 0:
        #         # if (left) % wt[0] == 0:
        #         return (left // wt[0]) * val[idx]
        #         # return float('-inf')
        #     take = val[idx] + rec(idx,left - (wt[idx]))
            
        #     not_t = rec(idx - 1,left)
            
        #     dp[(idx,left)] = max(not_t,take)
        #     return dp[(idx,left)]
            
        # return rec(N-1,W)
        dp = []
        for i in range(len(wt)):
            new_row = []
            for j in range(W+1):
                new_row.append(float("-inf"))
            dp.append(new_row)
        # print(dp)
        for left in range(W+1):
            # print(i * price[0],dp[0][i])
            dp[0][left] = (left // wt[0]) * val[0]
        
        for idx in range(1,len(wt)):
            for left in range(W+1):
                not_t = dp[idx - 1][left]
                take = float('-inf')
                if left - (wt[idx]) >= 0:
                    take = val[idx] + dp[idx][left - (wt[idx])]
                dp[idx][left] = max(not_t,take)
        return dp[-1][-1]
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends