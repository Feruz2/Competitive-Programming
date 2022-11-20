#User function Template for python3
from collections import defaultdict
class Solution:
    def cutRod(self, price, n):
        #code here
        # dp = defaultdict(int)
        # def rec(idx,left):
        #     if (idx,left) in dp:
        #         return dp[(idx,left)]
        #     if left < 0:
        #         return float('-inf')
        #     if idx == 0:
        #         return left * price[idx]
            
        #     take = price[idx] + rec(idx,left - (idx + 1))
            
        #     not_t = rec(idx - 1,left)
        #     dp[(idx,left)] = max(not_t,take)
        #     return dp[(idx,left)]
            
        # return rec(len(price) - 1,n)
        dp = []
        for i in range(len(price)):
            new_row = []
            for j in range(n+1):
                new_row.append(float("-inf"))
            dp.append(new_row)
        # print(dp)
        for i in range(n+1):
            # print(i * price[0],dp[0][i])
            dp[0][i] = (i * price[0])
        
        for idx in range(1,len(price)):
            for left in range(n+1):
                not_t = dp[idx - 1][left]
                take = float('-inf')
                if left - (idx + 1) >= 0:
                    take = price[idx] + dp[idx][left - (idx + 1)]
                dp[idx][left] = max(not_t,take)
        return dp[-1][-1]
            
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends