class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        dicit = {x:"ab", y:"ba"}
        if x > y:
            pri = dicit[x]
            sec = dicit[y]
        else:
            pri = dicit[y]
            sec = dicit[x]
            
        st = []
        ans = 0
        for i in range(len(s)):
            if not st or st[-1] != pri[0]:
                st.append(s[i])
            elif st[-1] == pri[0] and s[i] == pri[1]:
                ans += max(x,y)
                st.pop()
            elif st[-1] == pri[0] and s[i] != pri[1]:
                st.append(s[i])
        # print(st,ans)
        s = st
        st = []
        for i in range(len(s)):
            if not st or st[-1] != sec[0]:
                st.append(s[i])
            elif st[-1] == sec[0] and s[i] == sec[1]:
                ans += min(x,y)
                st.pop()
            elif st[-1] == sec[0] and s[i] != sec[1]:
                st.append(s[i])
        return ans
        
        
                