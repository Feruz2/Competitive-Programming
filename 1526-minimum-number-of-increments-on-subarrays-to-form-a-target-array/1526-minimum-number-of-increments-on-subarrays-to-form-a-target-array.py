class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        st = []
        ans = 0
        num = 0
        
        for i in range(len(target)):
            if st and st[-1] < target[i]:
                ans += (st[0] - num)
                num =  st.pop()
                st = []
            st.append(target[i])
            
        if st: ans += (st[0] - num)
        return ans
            