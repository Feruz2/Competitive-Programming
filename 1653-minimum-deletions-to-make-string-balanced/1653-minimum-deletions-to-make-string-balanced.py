class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        st = []
        for i in range(len(s)):
            if st and st[-1] == "b" and s[i] == "a":
                st.pop()
                ans += 1
            else:
                st.append(s[i])
        return ans