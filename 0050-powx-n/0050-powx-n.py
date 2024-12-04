class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def rec(x,n):
            
            if n > 1 and n % 2 == 0:
                print(n)
                ans =  rec(x, n // 2) 
                return ans * ans
            
            elif n > 1 and n % 2 != 0:
                ans =  rec(x, (n - 1) // 2) 
                return ans * ans * x
                print(n)
            
            return x 
        
        if n == 0:
            return 1
        
        if n > 0: 
            return rec(x,n)
        
        return 1/rec(x, n * - 1)
