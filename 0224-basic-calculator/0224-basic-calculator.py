class Solution:
    def calculate(self, string: str) -> int:
        st = []
        ans = 0
        i = len(string) - 1
        while i >= 0:
            # print(st,i, string[i])
            if string[i] == " ":
                i -= 1
                continue

            elif 48 <= ord(string[i]) <= 58 :
                j = i - 1
                num = string[i]
                while j >= 0 and 48 <= ord(string[j]) <= 58:
                    new = string[j] + num
                    num = new
                    j -= 1
                st.append(num)
                # while j >= 0 and string[j] == " ":
                #     j -= 1
                # # print(j, "j")
                # if j == -1: 
                #     st.append(num)
                # elif string[j] == "+" or string[j] == "(" or string[j] == ")": 
                #     st.append(num)
                # elif string[j] == "-":
                #     st.append("-" + num)
                i = j
                # print(i, st)
            elif string[i] == ")":
                i -= 1
                st.append(")")

            elif string[i] == "(":
                ans = 0
                while st and st[-1] != ")":
                    num = st.pop()
                    ans +=  int(num)

                st.pop()
                st.append(str(ans))
                i -= 1
            elif string[i] == "-":
                temp = []
                curr = 0
                while st:
                    curr = st.pop()
                    if curr == ")":
                        temp.append(curr)
                    else:
                        break
                
                st.append(str(int(curr) * - 1))
                # print(st, "end")
                while temp:
                    st.append(temp.pop())
                i -= 1
                
            else:
                i -= 1
        print(st)
        ans = 0
        while st:
            ans += int(st.pop())
        return ans