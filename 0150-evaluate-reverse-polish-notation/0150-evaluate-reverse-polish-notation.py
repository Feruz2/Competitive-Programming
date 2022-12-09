class Solution:
    def evalRPN(self, token: List[str]) -> int:
        s = []
        for i in range(len(token)):
            if token[i] in ["+","-","*","/"]:
                two = s.pop()
                one = s.pop()
                if token[i] == "+": 
                    s.append(int(one) + int(two))
                elif token[i] == "-":
                    s.append(int(one) - int(two))
                elif token[i] == "/":
                    s.append(int(int(one) / int(two)))
                else:
                    s.append(int(one) * int(two))
            else:
                s.append(token[i])
        return int(s[-1])