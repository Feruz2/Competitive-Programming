class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            ans = 1
            for i in range(2, n + 1):
                ans *= i
            return ans


        lst = []
        st = []
        for i in range(1, n + 1):
            lst.append(i) 
       
        def rec(n, k):
            
            if k == 0 or k == 1:
                return k
            
            total = factorial(n - 1)
           
            rem = math.ceil(float(k) / total)
           
            st.append(lst[int(rem) - 1])
           
            lst.remove(lst[int(rem) - 1])
            
            nextt = k % total
            return rec(n - 1, int(nextt))
        
        
        done = rec(n, k)
        print(st, done)
        if done: 
            st += lst
        else:
            st += lst[::-1]
        return "".join(map(str, st))