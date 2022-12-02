class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        
        one = sum(a)
        two = sum(b)
        s = set(a)
        for i in range(len(b)):
            temp_one = one + b[i]
            temp_two = two - b[i]
    
            if (temp_one - temp_two) % 2 == 0 and (temp_one-temp_two)//2 in s:
                return 1
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends