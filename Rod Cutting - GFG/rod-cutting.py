#User function Template for python3
from collections import defaultdict
class Solution:
    def cutRod(self, price, n):
        #code here
        dp = defaultdict(int)
        def rec(idx,left):
            if (idx,left) in dp:
                return dp[(idx,left)]
            if left < 0:
                return float('-inf')
            if idx == 0:
                return left * price[idx]
            
            take = price[idx] + rec(idx,left - (idx + 1))
            
            not_t = rec(idx - 1,left)
            dp[(idx,left)] = max(not_t,take)
            return dp[(idx,left)]
            
        return rec(len(price) - 1,n)

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